from __future__ import unicode_literals
from django.db import models
import uuid


def gen_rand_filename(instance, filename):
    """Generate a unique filename for uploaded file or image."""
    extension = filename.split(".")[-1]
    return "documents/{}.{}".format(uuid.uuid4(), extension)


class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100, blank=True, default='')
    email = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ('created',)


class Phrase(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    phrase = models.TextField()
    phrase_lang = models.CharField(default='en-US', max_length=100)
    translation = models.TextField()
    translation_lang = models.CharField(default='es-MX', max_length=100)
    user = models.ForeignKey('User', related_name="phrase")

    class Meta:
        ordering = ('created',)


class Photo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    # image = models.ImageField(upload_to='documents/')
    image = models.ImageField('Uploaded Image', upload_to=gen_rand_filename)
    phrase = models.TextField(default='new')
    phrase_lang = models.CharField(default='en-US', max_length=100)
    user = models.ForeignKey('User', related_name="photo")

    class Meta:
        ordering = ('created',)
