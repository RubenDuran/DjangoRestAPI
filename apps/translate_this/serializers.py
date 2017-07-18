from rest_framework import serializers
from . models import User, Phrase, LANGUAGE_CHOICES


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'created',)

class PhraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phrase
        fields = ('id','phrase', 'phrase_lang', 'translation', 'translation_lang', 'user', 'created')
