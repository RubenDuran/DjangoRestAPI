from __future__ import unicode_literals
from django.db import models


class ImageManager(models.Manager):

    def img_to_text(self, post):
        errors = []
        # if len(post['prod_name']) < 1:
        #     errors.append('Field may not be empty')
        # if len(post['prod_name']) < 3:
        #     errors.append(
        #         'Product/Item name must be at least 3 characters long')
        # check_product = self.filter(prod_name=post['prod_name'])
        # if check_product:
        #     errors.append('Product already exist in the database')
        return errors


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


class Image(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        max_length=None, allow_empty_file=False, upload_to='documents/')
    # phrase = models.TextField()
    # phrase_lang = models.CharField(default='en-US', max_length=100)
    # translation = models.TextField()
    # translation_lang = models.CharField(default='es-MX', max_length=100)
    user = models.ForeignKey('User', related_name="image")
    objects = ImageManager()

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
