from django.contrib import admin
from homeBuild.jobs.models import Job
from homeBuild.photos.models import Photo

class PhotoAdmin(admin.ModelAdmin):
    list_display = ['user', 'job', 'project', 'date_of_publication']
    list_filter = ['job', 'project', 'user']

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Job)