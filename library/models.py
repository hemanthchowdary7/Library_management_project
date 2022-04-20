from django.db import models
from django_countries.fields import CountryField
from django.urls import reverse

# Create your models here.

#Gener Model
class Category(models.Model):
    name = models.CharField(max_length=20)

    # Methods
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

# Author Model
class Author(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="photos", default='download.png')
    country = CountryField(blank_label='(select country)')

    # Methods
    def __str__(self):
        return self.name + ' ' + self.surname + ' from ' + self.country.name

    def get_absolute_url(self):
        return reverse("author_detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ['surname']

class Book(models.Model):
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20)
    cover = models.ImageField(upload_to='book_cover', default='download.png')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    categories = models.ManyToManyField(Category)

    # Methods
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
