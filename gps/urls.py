from django.urls import path
from .views import GPSList, GPSDetail, check


urlpatterns = [
    path('', GPSList.as_view()),
    path('<int:pk>/', GPSDetail.as_view()),
    path('check/', check),
]