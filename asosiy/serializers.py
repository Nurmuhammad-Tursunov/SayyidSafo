from rest_framework.serializers import ModelSerializer
from .models import *


class TopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class AudioSerializer(ModelSerializer):
    topic = TopicSerializer()
    class Meta:
        model = Audio
        fields = '__all__'