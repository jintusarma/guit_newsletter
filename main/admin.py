from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display= ('image_tag','title','description','url','add_date')
    search_fields= ('title',)
    
    def __str__(self):
        return self.title
    
admin.site.register(Catergory,CategoryAdmin)


# admin.site.register(Catergory)

class PostAdmin(admin.ModelAdmin):
    list_display= ('image_tag','title','author','status','add_date')
    search_fields= ('title',)
    list_filter = ('cat',)
    list_per_page= 10
admin.site.register(Post,PostAdmin)