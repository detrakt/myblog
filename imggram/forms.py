from django.forms import ModelForm
from models import ImgPost

class ImgForm(ModelForm):
	class Meta:
		model = ImgPost
		fields = ['image', 'title', 'description']
		#exclude = ['user', 'id', 'created_at', 'updated_at']