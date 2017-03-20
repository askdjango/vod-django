from django import forms
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post


post_list = ListView.as_view(model=Post, paginate_by=10)

post_detail = DetailView.as_view(model=Post)

post_new = CreateView.as_view(model=Post)

post_edit = UpdateView.as_view(model=Post, fields='__all__')

post_delete = DeleteView.as_view(model=Post, success_url='/blog/')

