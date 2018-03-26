from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.db import models
from ..users.models import User

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class BookManager(models.Manager):
    def validate(self,post_data):
        if "title" not in post_data:
            raise ValidationError("Must have a title!")
        if "author" not in post_data and "author_add" not in post_data:
            raise ValidationError("Must have an author!")
        return self

    def create_book(self,post_data):
        if "author_add" in post_data:
            author_name = post_data["author_add"]
        else:
            author_name = post_data["author"]
        try:
            author = Author.objects.get(name=author_name)
        except:
            author = Author.objects.create(name=author_name)
        return self.create(
            title = post_data["title"],
            author = author
        )


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author,related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

class ReviewManager(models.Manager):
    def validate(self,post_data):
        if "review" not in post_data:
            raise ValidationError("Please add a review")
        if "rating" not in post_data:
            raise ValidationError("Please add a rating")
        return self

    def create_review(self,book,user,post_data):
        return self.create(
            review = post_data["review"],
            rating = post_data["rating"],
            book = book,
            user = user
        )

class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    book = models.ForeignKey(Book,related_name="reviews")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,related_name="reviews",default="no reviews")
    objects = ReviewManager()
