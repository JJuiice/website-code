from django.shortcuts import render
from blog.models import Post, Comment


# Create your views here.
def posts_list(request):
    posts = Post.objects.all()

    context = {
        "posts": posts
    }

    return render(request, "posts_list.html", context)


def filtered_posts_list(request, topics):
    posts = Post.objects.filter(topics__name=topics)

    context = {
        "posts": posts
    }

    return render(request, "posts_list.html", context)


def posts_details(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)

    context = {
        "post": post,
        "comments": comments
    }

    return render(request, "posts_details.html", context)
