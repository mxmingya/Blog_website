from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
#for every time we modify models.py this file, we need to run
#python3 manage.py makemigrations
#python3 manage.py migrate
class Post(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField(max_length = 800)
    image = models.FileField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
    #these little shit will put the timestamp in the database automatically

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail',kwargs={'id':self.id})
