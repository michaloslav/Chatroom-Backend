from django.contrib import admin

# Register your models here.
from .models import ChatMessages

admin.site.register(ChatMessages)