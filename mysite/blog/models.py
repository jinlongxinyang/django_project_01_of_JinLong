from __future__ import unicode_literals

from django.db import models

from django.contrib import admin

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')

admin.site.register(BlogPost, BlogPostAdmin)
#########################################

class Author(models.Model):
    name = models.CharField(max_length=100)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Author, AuthorAdmin)
#########################################

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author)
    #authors = models.ManyToManyField(Author)
    length = models.IntegerField()

    class Meta:
        ordering = ['title']

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'length')

admin.site.register(Book, BookAdmin)
#########################################
class Person(models.Model):
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    middle = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ['last', 'first', 'middle']
        unique_together = ['first', 'last', 'middle']
        verbose_name_plural = 'people'

class PersonAdmin(admin.ModelAdmin):
    list_display = ('first', 'middle', 'last')

admin.site.register(Person, PersonAdmin)
#########################################


#########################################
#######
#########################################
print 'book.objects.all():', Book.objects.all()
book = Book.objects.get(title='book2')
author = book.author.name
title = book.title
print '@@@@@@@@@@@book,author:', title, author
#books = book.author.book_set.all()
#books = book.author.book_set.all()

lincoln_family = Person.objects.filter(middle='lincoln')
print 'lincoln_family:',lincoln_family 
abraham = lincoln_family.filter(first='abraham')
print 'abraham:',abraham
print 'id(abraham[0]):',id(abraham[0]) 
abraham[0].last = 'lincoln'
print 'abraham[0].__dict__:', abraham[0].__dict__

print Person.objects.values('first')
print Person.objects.values_list('first')

for person in lincoln_family:
    print id(person), person.first, person.last


#########################################
