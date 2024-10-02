from django.utils import timezone
from django.shortcuts import get_object_or_404, render

from blog.models import Post, Category
from .constants import NUM_LATEST_POSTS


def index(request):
    template = 'blog/index.html'
    now = timezone.now()
    posts = Post.objects.filter(pub_date__lt=now, is_published=True,
                                category__is_published=True
                                ).order_by('-pub_date')[:NUM_LATEST_POSTS]
    context = {'post_list': posts}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    now = timezone.now()
    post = get_object_or_404(Post, pk=id, pub_date__lte=now, is_published=True,
                             category__is_published=True)

    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    now = timezone.now()
    category = get_object_or_404(Category, slug=category_slug,
                                 is_published=True)
    post_list = category.posts.filter(is_published=True, pub_date__lte=now)
    context = {'category': category,
               'post_list': post_list}
    return render(request, template, context)
