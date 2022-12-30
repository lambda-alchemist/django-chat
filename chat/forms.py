from django.forms import ModelForm

from chat.models import Profile

class ProfileForm(ModelForm):
	class Meta:
		fields = ['picture']
