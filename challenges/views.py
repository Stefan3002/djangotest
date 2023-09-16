from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView

from challenges.models import Review, Post


class indexViews(ListView):
    template_name = "index.html"
    model = Post
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = context.get('posts')[:3]
        return context


class singlePostView(DetailView):
    template_name = 'single.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Post.objects.all().filter(title=self.object.title).tags
        return context


class februaryView(DetailView):
    template_name = 'challenges/index.html'
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_object = self.object
        request = self.request
        context['is_favorite'] = request.session.get('favorite_review') == str(loaded_object.id)
        return context
