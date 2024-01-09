from django.db import models
from autoslug import AutoSlugField
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    Category_Name = models.CharField(max_length=100) 


    def __str__(self):
        return self.Category_Name

class BlogCreate(models.Model):
    Title =models.CharField(max_length=200)
    Content =models.TextField()
    description =models.TextField(null=True)
    Key_Word =models.CharField(max_length=400 ,null=True)
    Status =models.BooleanField(default=True,help_text="0-Show ,1-Hide",null=True)
    Trending = models.BooleanField(default=False,help_text="0-False ,1-True",null=True)
    Create_Time =models.DateTimeField(auto_now_add=True)
    Image =models.ImageField(blank=True ,null=True ,upload_to='Uploads/')
    Category= models.ForeignKey(Category , related_name="Category",on_delete=models.CASCADE)
    Slug=AutoSlugField(populate_from='Title',unique=True, blank=True)
    

    # def save(self, *args, **kwargs):
    #      if not self.Slug:
    #         self.Slug = slugify(self.Title)
    #         super(BlogCreate, self).save(*args, **kwargs)

    

    def __str__(self):
        return self.Title

