from django.db import models

class Author(models.Model):
	AuthorID = models.CharField(primary_key=True, max_length = 50)
	Name = models.CharField(max_length = 50)
	Age = models.CharField(max_length = 50)
	Country = models.CharField(max_length = 50)
class Book(models.Model):
    ISBN = models.CharField(primary_key=True, max_length = 50)
    Title = models.CharField(max_length = 50)
    AuthorID = models.ForeignKey(Author)
    Publisher = models.CharField(max_length = 50)
    PublishDate = models.DateField()
    Price = models.CharField(max_length = 50)
# modify 3
