from django.contrib import admin
from .models import Form


class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name", "email") # it allows search using any of the parameters
    list_filter = ("date", "occupation") # it filters by date or occupation
    ordering = ("first_name", )  # it sort it in alphabetical order
    readonly_fields = ("occupation", ) # this prevents the admin from modifying any of perimeters mentioned


admin.site.register(Form, FormAdmin)
