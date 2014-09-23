from django.db import models
from django import forms
from urls.settings import DOMAIN
maxUrlDisplay = 40


class Url(models.Model):
    long = models.URLField()
    short = models.CharField(max_length=6)

    
    def get_absolute_url(self):
        return 'http://' + DOMAIN + '/' + self.short

   

class UrlForm(forms.Form):
    long = forms.URLField()
