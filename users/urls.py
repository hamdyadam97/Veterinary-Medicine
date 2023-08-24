from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('create/', views.create_user, name='create_user'),
    path('create_user_type/', views.create_user_type, name='create_user_type'),
    path('create_address_user_type/<str:slug>/', views.create_user_type_address, name='create_address_user_type'),
    path('<int:user_id>/update/', views.update_user, name='update_user'),
    path('<int:user_id>/', views.user_detail, name='user_detail'),
    path('login/', views.user_detail, name='login'),
]