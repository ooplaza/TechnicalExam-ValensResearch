from django.db import models
from django.urls import reverse

# Create your models here.
class CarColor(models.Model):
    colors = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.colors

class Car(models.Model):
    car_name = models.CharField(max_length=50)
    car_model = models.CharField(max_length=200)
    car_description = models.TextField(max_length=200)
    car_color = models.ForeignKey(CarColor, on_delete=models.CASCADE)
    date_manufactured = models.DateTimeField(auto_now_add=True)
    
    def get_absolute_url(self):
        """ After creating a Car, this function will be triggered and redirection using reverse"""
        return reverse("car_detail", kwargs={"pk": self.pk})
    
    class Meta:
        ordering = ['date_manufactured']

    def __str__(self):
        return f'{self.car_name}'