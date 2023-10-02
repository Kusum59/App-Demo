from django.urls import path 
from .import views 
urlpatterns = [
    path('test', views.FirstApiTestView.as_view(), name='test') 
]