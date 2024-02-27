from django.urls import path
from Myapp import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('about/', views.About, name='about'),
    path('contact/', views.Contact, name='contact'),
    path('chocolate/', views.Chocolate, name='chocolate'),
    path('testimonial/', views.Testimonial, name='testimonial')
]
