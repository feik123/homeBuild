from decimal import Decimal

from django.db import models
from homeBuild.common.utils import haversine
from math import cos, radians

class JobManager(models.Manager):
    def nearby(self, latitude, longitude, radius_km=30):
        latitude = float(latitude)
        longitude = float(longitude)

        # Approximate degree deltas for bounding box
        lat_delta = radius_km / 111.0
        lon_delta = radius_km / (111.0 * cos(radians(latitude)))

        candidates = self.get_queryset().filter(
            latitude__isnull=False,
            longitude__isnull=False,
            latitude__gte=Decimal(latitude - lat_delta),
            latitude__lte=Decimal(latitude + lat_delta),
            longitude__gte=Decimal(longitude - lon_delta),
            longitude__lte=Decimal(longitude + lon_delta),
        )

        nearby_jobs = []
        for job in candidates:
            distance = haversine(latitude, longitude, float(job.latitude), float(job.longitude))
            if distance < radius_km:
                job.distance = round(distance, 2)
                nearby_jobs.append(job)

        return sorted(nearby_jobs, key=lambda job: job.distance)
