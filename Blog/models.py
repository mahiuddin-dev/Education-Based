from django.db import models
from taggit.managers import TaggableManager
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

# Post model
class Blog_Post(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey('Category_List',related_name="products",on_delete=models.CASCADE)
    body = models.TextField()
    tags = TaggableManager()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog/', blank=True, null=True,)
    image_url = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(unique=True)
    read = models.IntegerField(default=0)
    tranding = models.IntegerField(default=0)
    tranding_date = models.DateTimeField(auto_now_add=True)
    home_slider = models.BooleanField(default=False)
    feature_news = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']
    
    # post url
    def get_absolute_url(self):
        return f"/blog/{self.slug}"


class Category_List(MPTTModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    parent = TreeForeignKey('self',blank=True,null=True,related_name='child',on_delete=models.CASCADE)

    class Meta:
        unique_together = ('slug', 'parent',)    
        verbose_name_plural = "categories"   
    
    def get_absolute_url(self):
        return f"/blog/category/{self.pk}"

    def __str__(self):                           
        full_path = [self.name]            
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' -> '.join(full_path[::-1])

# Comment model
class Post_Comment(models.Model):
    post = models.ForeignKey(Blog_Post, on_delete= models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    email = models.CharField(max_length=150)
    creation = models.DateTimeField(auto_now_add=True)
    approve = models.BooleanField(default=False)




