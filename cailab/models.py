from django.db import models
from django.urls import reverse
from django.utils.dateformat import DateFormat
from datetime import datetime
from django import forms

class UploadFileForm(forms.Form):
    name = forms.CharField(max_length=15)
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, help_text="글의 종류 입력")

    def __str__(self):
        return self.name

class Biography(models.Model):
    kr_name = models.CharField(max_length=20, default=str)
    eng_name = models.CharField(max_length=200, default=str)
    images = models.ImageField(upload_to="photo")
    content = models.TextField()
    email = models.EmailField(default=str)
    interest_first = models.CharField(max_length=50, default=str)
    interest_second = models.CharField(max_length=50, default=str)
    interest_third = models.CharField(max_length=50, default=str, blank=True)
    link_address = models.URLField(max_length=200, default=str, blank=True)

    def __str__(self):
        return self.eng_name
    
    def get_absolute_url(self):
        return reverse("student", args=[str(self.id)])

class Post(models.Model):
    title = models.CharField(max_length=200)
    files = models.FileField(blank=True, upload_to='files/')
    content = models.TextField()
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post", args=[str(self.id)])
    
    def modify_date_form(self):
        date = str.split(str(self.createDate))
        return date[0]
    