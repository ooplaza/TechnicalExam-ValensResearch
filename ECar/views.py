from django.shortcuts import render
from .models import Car
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

# Create your views here.
# Using Class Based View for CRUD Implementation
class HomePage(ListView):
    """ This class returns a List of Created cars but paginated. """
    model = Car
    template_name = 'html/homepage.html'
    context_object_name = 'cars'
    paginate_by = 3


class CarsList(ListView):
    """ This class returns a List of Created cars but this time paginated and much more on details. """
    model = Car
    template_name = 'html/cars.html'
    context_object_name = 'cars'


class RedCarList(ListView):
    """ Return List of the Red Cars. """
    model = Car
    template_name = 'html/red_cars.html'
    queryset = Car.objects.filter(car_color__colors='Red')
    context_object_name = 'cars'
    
    
class BlueCarList(ListView):
    """ Return List of the Blue Cars. """
    model = Car
    template_name = 'html/blue_cars.html'
    queryset = Car.objects.filter(car_color__colors='Blue')
    context_object_name = 'cars'

class MoveCars(ListView):
    model = Car
    template_name = 'html/move_cars.html'
    context_object_name = 'cars'
    
class CarDetail(DetailView):
    """ Return a detail view of a specific ECar. """
    model = Car
    template_name = 'html/car.html'
    context_object_name = 'car'
    

class CreateCar(LoginRequiredMixin, CreateView):
    """ This class is responsible for creating a Car, it has also a Authentication"""
    model = Car
    template_name = 'html/create.html'
    fields = ['car_name', 'car_model', 'car_description','car_image', 'car_color']

    def form_valid(self, form):
        car_name = form.cleaned_data['car_name']
        messages.success(self.request, f'Your have successfully created "{car_name}" model!')
        return super().form_valid(form)


class UpdateCar(LoginRequiredMixin, UpdateView):
    """ This class is responsible for Updating a Car, it has also a Authentication"""
    model = Car
    template_name = 'html/update.html'
    fields = ['car_name', 'car_model', 'car_description','car_image', 'car_color']

    def form_valid(self, form):
        car_name = form.cleaned_data['car_name']
        messages.warning(self.request, f'Your have successfully updated "{car_name}" model!')
        return super().form_valid(form)

class DeleteCar(LoginRequiredMixin, DeleteView):
    """ This class is responsible for Deleting a Specific Car, it has also a Authentication"""
    model = Car
    template_name = 'html/delete.html'
    success_url = reverse_lazy('cars_list')
    
    def delete(self, *args, **kwargs):
        messages.success(self.request, 'Your model was deleted successfully!')
        return super().delete(self.request, *args, **kwargs)