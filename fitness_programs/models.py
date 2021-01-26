from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  # seperate table so need to import


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)
    date_posted = models.DateTimeField(default=timezone.now)  # pass in func as default so no need for ()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  #args if user is deleted, then we delete

    def __str__(self):
        return self.title

    # dunder special/magic methods __str__ (self as arg) - we return how we want it to printed out ()
    # object oritenated focus


