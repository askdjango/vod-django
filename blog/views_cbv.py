from django import forms
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.forms import PostForm
from .models import Post


class PostListView(ListView):
    model = Post
    queryset = Post.objects.all().select_related('user').prefetch_related('tag_set', 'comment_set')
    paginate_by = 10

    def get_queryset(self):
        self.q = self.request.GET.get('q', '')
        qs = super().get_queryset()
        qs = qs.filter(title__icontains=self.q)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.q
        return context

post_list = PostListView.as_view()


post_detail = DetailView.as_view(model=Post)


@method_decorator(login_required, name='dispatch')
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user
        return super().form_valid(form)

post_new = PostCreateView.as_view()


post_edit = UpdateView.as_view(model=Post, fields='__all__')

post_delete = DeleteView.as_view(model=Post, success_url=reverse_lazy('blog:post_list'))

