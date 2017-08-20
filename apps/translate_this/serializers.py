from rest_framework import serializers
from . models import User, Phrase, Image


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'created')


class PhraseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Phrase
        fields = ('id', 'phrase', 'phrase_lang', 'translation',
                  'translation_lang', 'user', 'created')


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('id', 'image', 'user', 'created')
        # fields = ('id', 'phrase', 'phrase_lang', 'translation',
        #           'translation_lang', 'user', 'created')
