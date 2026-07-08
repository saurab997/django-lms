from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=20)
    bio = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=20)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(unique=True , max_length=20)
    published_date = models.DateField(blank=True, null=True)
    copies_total = models.PositiveIntegerField()
    copies_available = models.PositiveIntegerField()

    def __str__(self):
        return self.title
    
    @property
    def is_available(self):
        return self.copies_available > 0
