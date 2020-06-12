from django.urls import path
from . import views


app_name = 'learn_app'


urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]