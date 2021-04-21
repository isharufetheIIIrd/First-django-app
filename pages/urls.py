from django.urls import path
from .views import homePageView
urlpatterns = [
path('homePageView/', homePageView, name='home'),
]