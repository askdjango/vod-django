from django import forms
from django.views.generic import ListView, CreateView
from .models import Post


post_list = ListView.as_view(model=Post, paginate_by=10)


# blog/forms.py
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    # success_url = '/...'

post_new = PostCreateView.as_view()
