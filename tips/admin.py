from django.contrib import admin

from tips.models import Tip
from tips.models import UserProfile

admin.site.register(Tip)
admin.site.register(UserProfile)
