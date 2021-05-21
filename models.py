from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from django.db.models.signals import pre_save






class post(models.Model):
    Project_name  = models.CharField(max_length=100)
    Content = models.TextField(default = 'About the project')
    dateposted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User , on_delete = models.CASCADE)
    Brief = models.CharField(max_length=100)
    Image = models.ImageField()
    Link = models.CharField(max_length=300)
    slug = models.SlugField(max_length = 250,null=True,blank=True)
    upvotes = models.ManyToManyField(User,related_name='upvotes')
    
    TAGS = [
            ('PUBLIC',('PUBLIC')),
            ('PRIVATE', ('PRIVATE')),
            ]
    TAGS = models.CharField(
        max_length=32,
        choices = TAGS,
        default = 'N/A',
        
    )
    
    def __str__(self):
        return self.title 
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
    @property
    def totalupvotes(self):
        return self.upvotes.all().count()





class Rating(models.Model):   
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(post,related_name="ratings",on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=now)
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
