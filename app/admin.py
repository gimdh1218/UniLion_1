from django.contrib import admin
from .models import Gift
from .models import Notice

# Register your models here.
admin.site.register(Gift)
admin.site.register(Notice)