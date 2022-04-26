from django import forms
from django.core.exceptions import ValidationError

from .models import Post

class PostForm(forms.ModelForm):

   class Meta:
       model = Post
       fields = ['author',
                 'categoryType',
                 'postTitle',
                 'postText']

   def clean(self):
       cleaned_data = super().clean()
       descriptionTitle = cleaned_data.get("postTitle")
       descriptionText = cleaned_data.get("postText")
       if descriptionTitle in descriptionText:
           raise ValidationError("Text must not match the title")

       return cleaned_data