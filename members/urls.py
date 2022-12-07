from django.urls import path
# from . import views
from .views import UserRegisterView

urlpatterns = [
    path('sign-up/',UserRegisterView.as_view(),name='sign-up/'),
]