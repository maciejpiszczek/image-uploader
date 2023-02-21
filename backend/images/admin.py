from django.contrib import admin

from images import models


admin.site.register(models.Image)
admin.site.register(models.Thumbnail)
