from django.contrib import admin

from .models import ModelClass
class AdminModel(admin.ModelAdmin):
    list_display = ('name','id','email')
    list_filter = ('name','id','email')


admin.site.register(ModelClass,AdminModel)