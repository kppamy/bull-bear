from django.contrib import admin

from bull_bear import models

# Register your models here.
admin.site.register(models.Gamble)
admin.site.register(models.Option)