#  Copyright (c) 2020-2021 Ojas Anand.
#
#  This file is part of GNU package. GNU package is free software: you can redistribute it and/or modify it under the
#  terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version. GNU package is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
#  PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of
#  the GNU General Public License along with this program. If not, see https://www.gnu.org/licenses/.

from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from blog.models import Post, Comment


class PostsListView(View):
    def get(self, request):
        topics_key = 'topics'
        posts = Post.objects.filter(
            topics__name=request.GET[topics_key]) if topics_key in request.GET else Post.objects.all()

        context = {
            "posts": posts
        }

        if request.is_ajax():
            output = JsonResponse({"success": True, "url": request.build_absolute_uri(request.get_full_path()),
                                   "posts": list(posts.values_list('name', flat=True))})
        else:
            output = render(request, "posts_list.html", context)

        return output


class PostsDetailsView(View):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        comments = Comment.objects.filter(post=post)

        context = {
            "post": post,
            "comments": comments
        }

        return render(request, "posts_details.html", context)
