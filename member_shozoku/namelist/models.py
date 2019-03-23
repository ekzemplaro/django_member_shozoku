from django.db import models
from django.urls import reverse

class Member(models.Model):
    name = models.CharField(max_length=30)
    year_of_birth = models.IntegerField(null=True)

    syozoku = models.ForeignKey('Syozoku', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('member-detail', args=[str(self.id)])

class Syozoku(models.Model):
    name = models.CharField(max_length=30)
    home = models.CharField(max_length=30)

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('syozoku-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.name}'
