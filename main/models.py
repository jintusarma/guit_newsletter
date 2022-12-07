from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField
from django.utils.html import format_html
from django.urls import reverse

# Create your models here.

class Catergory(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to ='category/')
    add_date = models.DateTimeField(auto_now_add=True)
    
    def image_tag(self):
        return format_html('<img src = "/media/{}"  style="width:30px;height:30px;border-radius:50%;" />'.format(self.image))
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('home')
        # return reverse('home', args= (str(self.cat_id)))

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200,)
    # content = HTMLField()
    content = RichTextField()
    # url = models.CharField(max_length=100)
    image = models.ImageField(upload_to ='post/',)
    cat = models.ForeignKey(Catergory,on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    add_date = models.DateTimeField(auto_now_add=True)
    add_date.editable = True
    
    def image_tag(self):
        return format_html('<img src = "/media/{}"  style="width:30px;height:30px;border-radius:50%;" />'.format(self.image))
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-add_date',)
