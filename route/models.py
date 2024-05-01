from django.contrib.auth.models import User
from django.db import models


class Vehicle(models.Model):
    vehicle_id = models.CharField(max_length=20)
    vehicle_number = models.CharField(max_length=50)
    model = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.vehicle_number}{self.model}"


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    driver_id = models.CharField(max_length=20)
    company = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username


class Route(models.Model):
    name = models.CharField(max_length=100)
    start_destination = models.CharField(max_length=100, default="")
    end_destination = models.CharField(max_length=100, default="")
    description = models.TextField(max_length=100)

    def __str__(self):
        return f"{self.name}{self.start_point}{self.end_point}{self.description}"


class Assignment(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    assigned_date = models.DateField()

    def __str__(self):
        return f"{self.vehicle.vehicle_number} assigned to {self.route.name} on {self.assigned_date}"
