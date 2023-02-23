from django.contrib import admin

from expiring_links import models


admin.site.register(models.ExpiringLink)
