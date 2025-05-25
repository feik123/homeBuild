from http.client import responses

from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from rest_framework.views import APIView, Response

from homeBuild import settings
from homeBuild.jobs.forms import JobAddForm
from homeBuild.jobs.models import Job, JobPhoto
from homeBuild.jobs.serializers import JobSerializer


class CreateJobView(CreateView):
    model = Job
    form_class = JobAddForm
    template_name = 'jobs/create.html'
    success_url = reverse_lazy('job-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['google_maps_api_key'] = settings.GOOGLE_MAPS_API_KEY
        return context

    def get_profile_type(self):
        return self.request.user.profile_type

    def dispatch(self, request, *args, **kwargs):
        profile_type = self.get_profile_type()

        if profile_type != 'homeowner':
            return HttpResponseForbidden("You must be a home owner to post this job")

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.homeowner = self.request.user

        form.instance.latitude = self.request.POST.get('latitude')
        form.instance.longitude = self.request.POST.get('longitude')

        response = super().form_valid(form)

        for file in self.request.FILES.getlist('images'):
            JobPhoto.objects.create(job=self.object, image=file)

        return response

class JobListView(ListView):
    model = Job
    template_name = 'jobs/job_list.html'
    context_object_name = 'jobs'
    paginate_by = 8
    ordering = ['-date_of_publication']

    def get_queryset(self):
        queryset = Job.objects.select_related('homeowner__homeownerprofile').order_by('-date_of_publication')
        print(queryset.query)
        return  queryset


class NearbyJobsView(APIView):
    def get(self, request):
        try:
            lat = float(request.GET.get('lat'))
            lon = float(request.GET.get('lon'))
        except (TypeError, ValueError):
            return Response({'error': 'Invalid or missing latitude/longitude'}, status=400)

        try:
            radius_km = float(request.GET.get('radius', 30))
        except ValueError:
            radius_km = 30

        jobs = Job.objects.nearby(lat, lon, radius_km)
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)