from django.contrib import admin

# Register your models here.
from .forms import PostmodForm
from .models import Postmod
from .models import Refmod
from .models import Tabormod


class PostmodAdmin(admin.ModelAdmin):
	list_display = ["__str__", "author", "created_date"]
	form = PostmodForm
	# class Meta:
	# 	model = PostUp

admin.site.register(Postmod, PostmodAdmin)
admin.site.register(Tabormod)
admin.site.register(Refmod)