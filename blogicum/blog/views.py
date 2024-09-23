from django.http import Http404

from django.shortcuts import render


def index(request):
    template = 'blog/index.html'
    context = {'posts': reversed(posts)}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    post = next((post for post in posts if post['id'] == id), None)

    if post is None:
        raise Http404(f"Пост с id {id} не найден.")

    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    filtered_posts = [post for post in posts
                      if category_slug in post['category']]

    context = {'category': category_slug,
               'posts': filtered_posts}
    return render(request, template, context)
