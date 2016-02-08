from django import forms

from .models import Postmod
from .models import Tabormod

class PostmodForm(forms.ModelForm):
	class Meta:
		model = Postmod
		fields = ["title", "author", "text",
		 "published_date", "created_date"]

