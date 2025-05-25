from django.db import models
from homeBuild.common.utils import haversine


class JobManager(models.Manager):
    def nearby(self, latitude, longitude, radius_km=30):

        nearby_jobs = []
        for job in self.get_queryset():
            if job.latitude and job.longitude:
                distance = haversine(latitude, longitude, job.latitude, job.longitude)
                if distance < radius_km:
                    job.distance = round(distance, 2)
                    nearby_jobs.append(job)

            return sorted(nearby_jobs, key=lambda job: job.distance)
