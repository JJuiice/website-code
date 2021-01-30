from django.shortcuts import render, redirect
from django.http import JsonResponse
from blog.models import Post, Comment


# Create your views here.
def posts_list(request):
    topics_key = 'topics'
    posts = Post.objects.filter(topics__name=request.GET[topics_key]) if topics_key in request.GET else Post.objects.all()

    context = {
        "posts": posts
    }

    if request.is_ajax():
        output = JsonResponse({"success": True, "url": request.build_absolute_uri(request.get_full_path()), "posts": list(posts.values_list('name', flat=True))})
    else:
        output = render(request, "posts_list.html", context)

    return output


def posts_details(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)

    context = {
        "post": post,
        "comments": comments
    }

    return render(request, "posts_details.html", context)
