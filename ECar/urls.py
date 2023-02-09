from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('cars-list/', views.CarsList.as_view(), name='cars_list'),
    path('create-car/', views.CreateCar.as_view(), name='create_car'),
    path('car/<str:pk>/', views.CarDetail.as_view(), name='car_detail'),
    path('update-car/<str:pk>/', views.UpdateCar.as_view(), name='update_car'),
    path('delete-car/<str:pk>/', views.DeleteCar.as_view(), name='delete_car'),
    path('red-cars/', views.RedCarList.as_view(), name='red_cars'),
    path('blue-cars/', views.BlueCarList.as_view(), name='blue_cars'),
    path('move-cars/', views.MoveCars.as_view(), name='move_cars')
]