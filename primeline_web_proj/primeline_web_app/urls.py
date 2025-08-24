from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('careers/', views.careers, name='careers'),
    path('services/', views.services, name='services'),
    path('industries/', views.industries, name='industries'),
    path('insights/', views.insights, name='insights'),
    path('careers/<int:job_id>/', views.job_detail, name='job_detail'),
]
