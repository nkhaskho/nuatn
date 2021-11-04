from math import sin, cos, sqrt, atan2, radians

# approximate radius of earth in km
R = 6373.0

def get_distance(point1, point2):
    """
    return the distance (in m) between two geo points
    """
    dlon = radians(point2.longitude) - radians(point1.longitude)
    dlat = radians(point2.latitude) - radians(point1.latitude)
    a = sin(dlat / 2)**2 + cos(radians(point1.latitude)) * cos(radians(point2.latitude)) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c
