from django.forms import ModelForm
from .models import Post
…

class AddPost(ModelForm):
	class Meta:
		model = Post
		fields = ['category','tag','title','review','the_body','release_datetime','image_cover','url']
