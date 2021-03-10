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
from django.views.generic.list import ListView
from blog.models import Post, Comment


class PostListView(ListView):
    model = Post
    paginate_by = 10
    template_name = 'post_list.html'

    def get_queryset(self):
        topics_key = 'topics'

        queryset = super(PostListView, self).get_queryset()
        qs = queryset.filter(topics__name=self.request.GET[topics_key]) if topics_key in self.request.GET else queryset
        return qs


class PostsDetailsView(View):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        comments = Comment.objects.filter(post=post)

        context = {
            "post": post,
            "comments": comments
        }

        return render(request, "post_details.html", context)
