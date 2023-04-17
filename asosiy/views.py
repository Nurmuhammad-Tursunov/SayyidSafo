from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import *
from .models import *
from .serializers import *


# Topics
class TopicsListAPIView(ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class TopicAudiosApiView(APIView):
    def get(self, request, pk):
        audios = Audio.objects.filter(topic__id=pk)
        ser = AudioSerializer(audios, many=True)
        return Response(ser.data)


# Audios
class AudiosListAPIView(ListAPIView):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer

class AudiosRetrieveAPIView(RetrieveAPIView):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer

