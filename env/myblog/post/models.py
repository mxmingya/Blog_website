from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils import timezone
# Create your models here.
#for every time we modify models.py this file, we need to run
#python3 manage.py makemigrations
#python3 manage.py migrate


#Post.objects.all()
#Post.objects.create() all kinds of model managers
class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        #overwrite the default all
        return super(PostManager, self).filter(draft=False).filter(publish__lte(timezone.now()))

def upload_location(instance, filename):
    #parse the location according to the filename
    #this function does not accept filename setted with '.' in the name
    #base, extension = filename.split('.')
    return "%s/%s" %(instance.id, instance.id)

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)#the default number of django user is 1
    title = models.CharField(max_length=200)
    #slug = SlugField(unique=True)
    content = models.TextField(max_length=800)
    image = models.ImageField(upload_to=upload_location, height_field='height_field', width_field='width_field', null=True, blank=True)
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
    draft = models.BooleanField(default=False)
    publish = models.DateTimeField(auto_now=False, auto_now_add=False)
    #these little shit will put the timestamp in the database automatically
    objects = PostManager()#overwrite the objects of Post into PostManager
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail',kwargs={'id':self.id})
