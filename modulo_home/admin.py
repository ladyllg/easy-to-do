from django.contrib import admin
from .models import *

# Register your models here.
class TodoItemAdmin(admin.ModelAdmin):
	pass

class BackgroundFileAdmin(admin.ModelAdmin):
	pass

class CategoryAdmin(admin.ModelAdmin):
	pass

admin.site.register(TodoItem, TodoItemAdmin)
admin.site.register(BackgroundFile, BackgroundFileAdmin)
admin.site.register(Category, CategoryAdmin)