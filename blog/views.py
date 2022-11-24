from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView , DetailView
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
class BlogDetailsView(DetailView):
    model = Post
    template_name: str = 'post_detail.html'
    