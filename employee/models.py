from django.db import models


# Create your models here.
class Department(models.Model):
    title = models.CharField(max_length=100)


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    birthdate = models.DateField(null=True, blank=True)
    cv = models.FileField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
