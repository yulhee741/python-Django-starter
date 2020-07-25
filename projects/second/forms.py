# from django import forms
from django.forms import ModelForm
from second.models import Post
from django.utils.translation import gettext_lazy as _


# class PostForm(forms.Form):
#     title = forms.CharField(label="제목", max_length=10)
#     content = forms.CharField(label='내용', widget=forms.Textarea)

class PostForm(ModelForm):
    class Meta:
        model = Post
        # models.py의 포스트 클래
        fields = ['title', 'content']
        # 입력받고 싶은 필드
        labels = {
            'title' : _('제목을 입력해주세요.'),
            'content' : _('내용을 입력해주세'),
        }
        error_messages = {
            'name': {
                'max_length': _("제목이 너무 깁니다. 30자 이하로 해주세요.")
            }
        }
