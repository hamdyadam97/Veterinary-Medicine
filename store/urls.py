from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('create/', views.create_store, name='create_store'),
    path('list/', views.list_store, name='list'),

]