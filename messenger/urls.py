from django.urls import path
from . import views

urlpatterns = [
    path('', views.InboxView.as_view(), name='messenger_inbox'),  
    path('', views.InboxView.as_view(), name='inbox'),  
    path('send/', views.send_message, name='messenger_send'),
    path('send/', views.send_message, name='send_message'),  
]



