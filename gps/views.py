
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import GPS
from .serializers import GPSSerializer
from users.models import User

from datetime import datetime, timedelta
from .utils import get_distance

class GPSList(generics.ListCreateAPIView):
    queryset = GPS.objects.all()
    serializer_class = GPSSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('user_id',)

class GPSDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GPS.objects.all()
    serializer_class = GPSSerializer


@api_view(['POST'])
def check(request):

    times = 0
    user = User.objects.get(pk=request.data['user'])
    other = User.objects.get(pk=request.data['other'])

    # get all user gps positions where created within the last week
    user_positions = GPS.objects.filter(user_id=request.data['user'], 
        created_at__gt=datetime.today()-timedelta(days=7))
    # get all other user gps positions where created within the last week
    other_positions = GPS.objects.filter(user_id=request.data['other'], 
        created_at__gt=datetime.today()-timedelta(days=7)
    )

    # get user with less gps records (to prevent IndexError)
    if len(other_positions) < len(user_positions):
        other_positions, user_positions = user_positions, other_positions

    # for all gps position, increment times if distance < 100
    for pos in range(len(user_positions)):
        if get_distance(user_positions[pos], other_positions[pos]) < 100:
            times += 1 
            
    # HttpResponse return
    return Response({
        "user": user.full_name,
        "other": other.full_name,
        "times": times
    })

