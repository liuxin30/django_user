from django.contrib import admin

from .models import Info


# Register your models here.
# admin.site.register(Info)

@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'id_num', 'fee')
