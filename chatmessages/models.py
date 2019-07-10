from django.db import models
from datetime import datetime

# Create your models here.
class ChatMessages(models.Model):
  username = models.CharField(max_length=100)
  text = models.TextField()
  time = models.DateTimeField(default=datetime.now, blank=True)
  room = models.CharField(max_length=100, default='General')

  def __str__(self):
    return "%s: %s" % (self.username, self.text)[:100]

  class Meta:
    verbose_name_plural = 'ChatMessages'