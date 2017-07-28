from __future__ import unicode_literals

from django.db import models

# Create your models here.
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# LEXERS = [item for item in get_all_lexers() if item[1]]
# LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
# STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100, blank=True, default='')
    email = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ('created',)


class Phrase(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    phrase = models.TextField()
    phrase_lang = models.CharField(default='English', max_length=100)
    translation = models.TextField()
    translation_lang = models.CharField(default='Spanish', max_length=100)
    user = models.ForeignKey('User',related_name="phrase")


    class Meta:
        ordering = ('created',)

# class Snippet(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     title = models.CharField(max_length=100, blank=True, default='')
#     code = models.TextField()
#     linenos = models.BooleanField(default=False)
#     language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
#     style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    # class Meta:
    #     ordering = ('created',)
