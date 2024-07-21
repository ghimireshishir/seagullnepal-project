from django.db import models

class Package(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField(help_text="Duration in days")
    image = models.ImageField(upload_to='packages/')

    def __str__(self):
        return self.name

class Booking(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    start_date = models.DateField()
    end_date = models.DateField()
    number_of_people = models.IntegerField()

    def __str__(self):
        return f"{self.user_name} - {self.package.name}"
