from django import forms
from askdjango.widgets.naver_map_point_widget import NaverMapPointWidget
from .models import Post


class PostForm(forms.ModelForm):
    # dummy = forms.CharField(widget=NaverMapPointWidget(attrs={'width': "100%", 'height': 200}))

    class Meta:
        model = Post
        fields = ['title', 'content', 'photo', 'lnglat', 'tag_set']
        widgets = {
            'lnglat': NaverMapPointWidget(attrs={'width': 600, 'height': 300}),
        }

