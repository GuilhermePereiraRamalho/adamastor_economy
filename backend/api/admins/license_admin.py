from django.contrib import admin
from api.models.license_models import License

class LicenseAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    search_fields = ('name',)

admin.site.register(License, LicenseAdmin)