from django.contrib import admin
from .models import BillBoard, Rubric

# Register your models here.

class BillBoardAdmin(admin.ModelAdmin):
	list_display = ('title', 'content', 'price', 'published', 'rubric')
	list_display_links = ('title',)
	search_fields=('title','content')
	
		

admin.site.register(BillBoard, BillBoardAdmin)
admin.site.register(Rubric)