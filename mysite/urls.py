from django.urls import path
from . import views

urlpatterns = [    
    path('', views.index, name="index"),
    path('en_version/', views.en_version, name='en_version')
]