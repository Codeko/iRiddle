from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


RIDDLE_STATUS_PENDING=0
RIDDLE_STATUS_APPROVED=1
RIDDLE_STATUS_REJECTED=-1

RIDDLE_STATUS=(
    (RIDDLE_STATUS_PENDING,_("Pending")),
    (RIDDLE_STATUS_APPROVED,_("Approved")),
    (RIDDLE_STATUS_REJECTED,_("Rejected"))
)

VALORATION=((1,1),(2,2),(3,3),(4,4),(5,5))

class Tag (models.Model):
    name=models.CharField(max_length=30)

class Category (models.Model):
    name=models.CharField(max_length=30)


class Riddle (models.Model):
    slug=models.SlugField()
    name= models.CharField(max_length=40)
    author=models.ForeignKey(User)
    introduction =models.TextField()
    explanation=models.TextField()
    image_introduction=models.ImageField(upload_to='riddle',blank=True)
    image_explanation=models.ImageField(upload_to='riddle',blank=True)
    date=models.DateTimeField(auto_now_add=True)
    via=models.CharField(max_length=200)
    tags=models.ManyToManyField(Tag)
    categories=models.ManyToManyField(Category)
    status=models.SmallIntegerField(choices=RIDDLE_STATUS)
        
class Valoration (models.Model):
    difficulty=models.SmallIntegerField(choices=VALORATION)
    quality=models.SmallIntegerField(choices=VALORATION)
    user=models.ForeignKey(User)
    riddle=models.ForeignKey(Riddle)




    





