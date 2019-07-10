from .models import ChatMessages
from rest_framework import serializers

class ChatMessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChatMessages
        fields = ('id', 'url', 'username', 'text', 'time', 'room')