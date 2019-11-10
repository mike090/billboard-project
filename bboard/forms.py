from django.forms import ModelForm

from .models import BillBoard

class BillBoardForm(ModelForm):
	class Meta:
		model = BillBoard
		fields = ('title', 'content', 'price', 'rubric')