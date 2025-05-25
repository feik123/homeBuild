from rest_framework import serializers

from homeBuild.common.utils import geocode_address
from homeBuild.jobs.models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['homeowner', 'title','description','job_category','location','latitude','longitude']
        read_only_fields = ['latitude', 'longitude']

    def set_coordinates(self, validated_data):
        if 'location' in validated_data:
            lat, lon = geocode_address(validated_data['location'])
            if lat is None or lon is None:
                raise serializers.ValidationError('Address cannot be geocoded.')

            validated_data['latitude'] = lat
            validated_data['longitude'] = lon

    def create(self, validated_data):
        self.set_coordinates(validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        self.set_coordinates(validated_data)
        return super().update(instance, validated_data)


