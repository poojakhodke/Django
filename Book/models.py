from django.db import models
from django import forms
# app name - Book, model name- Book

class BookActiveManager(models.Manager):
    def get_queryset(self):
        return super(BookActiveManager, self).get_queryset().filter(is_deleted= 'N')

class BookInActiveManager(models.Manager):
    def get_queryset(self):
        return super(BookInActiveManager, self).get_queryset().filter(is_deleted= 'Y')

class Book(models.Model):
    name = models.CharField(max_length=100)
    author= models.CharField(max_length=100)
    qty = models.IntegerField()
    price =models.FloatField()
    is_published = models.BooleanField(default=False)
    is_deleted = models.CharField(max_length=1, default='N')
    active_objects = BookActiveManager()
    inactive_objects = BookInActiveManager()
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "bookinfo"



'''
venv) D:\VSCODE\Python\Django\Library>python manage.py shell
Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from Book.models import Book  
>>> Book.objects.all()
<QuerySet [<Book: Alchemist>, <Book: Wings of Fire>, <Book: Python>]>
>>> b = Book.objects.all()
>>> type(b)
<class 'django.db.models.query.QuerySet'>
>>> list(b)
[<Book: Alchemist>, <Book: Wings of Fire>, <Book: Python>]
>>> Book.objects.get(id=3) 
<Book: Python>
>>> Book.objects.create(name='ABC', author='PQR', qty=3,price=321)
<Book: ABC>
>>> b4= Book(name='ABC', author='PQR', qty=3,price=321)
>>> b4.save()
>>> b5 = Book.objects.get(id=5)
>>> b5.name = 'PQR'
>>> b5.save()
>>> b6 = Book.objects.get(id=6)
>>> b6.delete()
(1, {'Book.Book': 1})
>>>
'''

    