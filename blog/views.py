from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.cache import cache

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    key = f'post:{post_id}:views'

 
    if cache.get(key) is None:
        cache.set(key, 1)
    else:
        cache.incr(key)

    views = cache.get(key)

    return render(request, 'blog/post_detail.html', {'post': post, 'views': views})
