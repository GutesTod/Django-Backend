from django.contrib import admin
from .models import Tournament

from .models import Match
# Register your models here.
admin.site.register(Match)
admin.site.register(Tournament)