from rest_framework import serializers
from . models import User, Phrase, Photo


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'created')


class PhraseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Phrase
        fields = ('id', 'phrase', 'phrase_lang', 'translation',
                  'translation_lang', 'user', 'created')


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = ('id', 'image', 'email', 'user',
                  'phrase', 'phrase_lang', 'created')
        # fields = ('id', 'phrase', 'phrase_lang', 'translation',
        #           'translation_lang', 'user', 'created')
