from django.contrib import admin

from prototype.models import User
from prototype.models import EventUser
# Register your models here.

admin.site.register(User)
admin.site.register(EventUser)
