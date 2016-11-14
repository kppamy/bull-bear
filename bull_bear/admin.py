from django.contrib import admin

from bull_bear import models

# Register your models here.
admin.site.register(models.Event)
admin.site.register(models.Outcome)
admin.site.register(models.Profile)
