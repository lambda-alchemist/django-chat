from django.forms import ModelForm

class PictureForm(ModelForm):
	class Meta:
		fields = ['picture']
