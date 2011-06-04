from django.contrib.auth.models import User
from django.db import models

.
class Profile (models.Model):
    user=models.OneToOneField(User)
    language=models.CharField(max_length=5)
    picture=models.ImageField(upload_to='profile',blank=True)
    date_join=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now=True)


    
