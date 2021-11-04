from django.db import models
from users.models import User
from datetime import datetime

# Create your models here.
class GPS(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self) -> str:
        return f'[{self.user_id}]: {self.created_at} : {self.username}'


class GPSCheck(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    other = models.ForeignKey(User, on_delete=models.CASCADE, related_name='other')
    times = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.user}-{self.other}'