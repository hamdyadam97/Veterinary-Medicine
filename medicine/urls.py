from django.urls import path
from . import views

app_name = 'medicine'

urlpatterns = [
    path('create/', views.create_product, name='create_products'),

]