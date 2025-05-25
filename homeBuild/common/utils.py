import math
from django.conf import settings
from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(settings.OPENCAGE_API_KEY)

def geocode_address(address):
    results = geocoder.geocode(address)

    if results and len(results):
        geometry = results[0]['geometry']
        return geometry['lat'], geometry['lng']

    return None, None


def haversine(lat1, lon1, lat2, lon2):
    # Calculating the distance between 2 addresses

    # Earth radius in kilometers
    R = 6371.0

    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)

    d_phi = math.radians(lon2 - lon1)
    d_lambda = math.radians(lat2 - lat1)

    a = math.sin(d_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(d_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

