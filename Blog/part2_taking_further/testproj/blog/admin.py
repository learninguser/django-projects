from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from blog import models

# Apply summernote to all TextField in model.
class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

# Register your models here.
admin.site.register(models.Post, SomeModelAdmin)
admin.site.register(models.Category, SomeModelAdmin)