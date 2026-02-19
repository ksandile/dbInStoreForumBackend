from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import tUsers, tPost, tComments, tLikes, tAiModerationLogs

admin.site.register(tUsers)
admin.site.register(tPost)
admin.site.register(tComments)
admin.site.register(tLikes)
admin.site.register(tAiModerationLogs)
