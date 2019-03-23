from django.db import models

# Create your models here.
from django.urls import reverse

class Member(models.Model):
    name = models.CharField(max_length=100)
    year_of_birth = models.IntegerField()

    syozoku = models.ForeignKey('Syozoku', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('member-detail', args=[str(self.id)])

class Syozoku(models.Model):
    name = models.CharField(max_length=30)
    home = models.CharField(max_length=30)

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('syozoku-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name}'
