from django.db import models

# Create your models here.
class User(models.Model):

    username = models.CharField(max_length=255, unique=True, db_index=True)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return f'[{self.id}] {self.username}'
