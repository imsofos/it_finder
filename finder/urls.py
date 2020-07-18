from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('', views.index, name="index"),
    path('search/', views.search, name='search'),
    path('getProduct/<int:pk>', views.getProduct, name='getProduct'),
    path('editProduct/<int:pk>', views.editProduct, name='editProduct'),
]