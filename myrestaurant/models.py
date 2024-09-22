from django.db import models

class Dish(models.Model):
    CATEGORY_CHOICES = [
        ('Appetizers', 'Appetizers'),
        ('Main Courses', 'Main Courses'),
        ('Desserts', 'Desserts'),
        ('Drinks', 'Drinks'),
        ('Others', 'Others'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name
