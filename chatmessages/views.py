from django.shortcuts import render
from .models import ChatMessages
from rest_framework import viewsets
from .serializers import ChatMessageSerializer

class ChatMessageViewSet(viewsets.ModelViewSet):
  queryset = ChatMessages.objects.all().order_by('time')
  serializer_class = ChatMessageSerializer

  def get_queryset(self):
    room = self.request.query_params.get('room', None)
    if room is not None: return self.queryset.filter(room=room)
    else: return self.queryset