from django.db.models import Q
from django.utils import timezone

from django.shortcuts import get_object_or_404, render
from blog.models import Post, Category

now = timezone.now()


def index(request):
    template = 'blog/index.html'
    posts = Post.objects.filter(Q(pub_date__lt=now) & Q(is_published=True)
                                & Q(category__is_published=True)
                                ).order_by('-pub_date')[:5]
    context = {'post_list': posts}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    post = get_object_or_404(Post, pk=id, pub_date__lte=now, is_published=True,
                             category__is_published=True)

    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'

    category = get_object_or_404(Category, slug=category_slug,
                                 is_published=True)
    post_list = category.post_set.filter(is_published=True, pub_date__lte=now)
    context = {'category': category,
               'post_list': post_list}
    return render(request, template, context)
