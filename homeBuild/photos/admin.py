from django.contrib import admin
from homeBuild.jobs.models import Job
from homeBuild.photos.models import Photo

class PhotoAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_publication']
    list_filter = ['job', 'user']

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Job)