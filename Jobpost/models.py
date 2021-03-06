from django.db import models
from taggit.managers import TaggableManager

# Create your models here.

# Post model
class Job_Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    tags = TaggableManager()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='jobs/image', blank=True, null=True)
    file = models.FileField(upload_to='jobs/file', blank=True, null=True)
    slug = models.SlugField(unique=True)
    read = models.IntegerField(default=0)

    class Meta:
        ordering = ['-date']
    
    # post url
    def get_absolute_url(self):
        return f"/jobs/{self.slug}"

# Comment model
class Job_Comment(models.Model):
    post = models.ForeignKey(Job_Post, on_delete= models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    email = models.CharField(max_length=150)
    creation = models.DateTimeField(auto_now_add=True)
    approve = models.BooleanField(default=False)




