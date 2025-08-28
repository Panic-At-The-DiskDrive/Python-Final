from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about_view, name='about_page'),   
    path('about/edit/', views.edit_about, name='edit_about'),
]


