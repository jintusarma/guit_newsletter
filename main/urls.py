from django.urls import path,include
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('',Homeview.as_view(),name='home'),
    # path('home/', Homeview.as_view(), name = "home"),
    path('',views.home,name='home'),
    path('home/', views.home, name = "home"),
    path('load-more',views.load_more,name='load-more'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name="article-detail"),
    path('create-post/',views.create_post,name="create-post"),
    path('my_posts/',EditnDeletePost.as_view(),name="my-posts"),
    path('delete_post/',DeletePost.as_view(),name="delete-post"),
    path('admin_approval/',views.approve_post, name='admin_approval'),
    path('add-category/', AddCategory.as_view(), name="add-category"),   #class based view 
    path('view-category/', ViewCategory.as_view(), name="view-category"),   #class based view 
    path('category/<slug:url>', category),
    
    #pdf
    path('pdf/render_pdf_view',views.render_pdf_view,name='test'),
    path('pdf/',views.date_take,name='pdf'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)