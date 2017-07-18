from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


from . models import User, Phrase
from . serializers import UserSerializer, PhraseSerializer


@api_view(['GET', 'POST'])
def user_list(request, format=None):
    """
    List all users, or create a new user.
    """
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk, format=None):
    """
    Retrieve, update or delete a user instance.
    """
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def phrase_list(request, format=None):
    """
    List all phrases, or create a new phrase.
    """
    if request.method == 'GET':
        phrases = Phrase.objects.all()
        serializer = PhraseSerializer(phrases, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PhraseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def phrase_detail(request, pk, format=None):
    """
    Retrieve, update or delete a phrase instance.
    """
    try:
        phrase = Phrase.objects.get(pk=pk)
    except Phrase.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PhraseSerializer(phrase)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PhraseSerializer(phrase, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        phrase.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#
# @csrf_exempt
# def user_list(request):
#     """
#     List all users, or create a new user.
#     """
#     if request.method == 'GET':
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = UserSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
# @csrf_exempt
# def user_detail(request, pk):
#     """
#     Retrieve, update or delete a user.
#     """
#     try:
#         user = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = UserSerializer(user)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = UserSerializer(user, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         user.delete()
#         return HttpResponse(status=204)
#
#
#
#
#
#
#
# @csrf_exempt
# def phrase_list(request):
#     """
#     List all phrases, or create a new phrase.
#     """
#     if request.method == 'GET':
#         phrases = Phrase.objects.all()
#         serializer = PhraseSerializer(phrases, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = PhraseSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
# @csrf_exempt
# def phrase_detail(request, pk):
#     """
#     Retrieve, update or delete a phrase.
#     """
#     try:
#         phrase = Phrase.objects.get(pk=pk)
#     except Phrase.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = PhraseSerializer(phrase)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = Phrase.Serializer(phrase, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         user.delete()
#         return HttpResponse(status=204)
