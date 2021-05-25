from django.contrib import admin
from detail_app.models import Detail

class DetailAdmin(admin.ModelAdmin):
  pass

# Register your models here.
admin.site.register(Detail, DetailAdmin)