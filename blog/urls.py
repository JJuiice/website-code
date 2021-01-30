from django.urls import path
from blog import views

urlpatterns = [
    path("", views.posts_list, name="posts_list"),
    path("<slug:topics>", views.filtered_posts_list, name="filtered_posts_list"),
    path("<int:pk>/", views.posts_details, name="posts_details")
]
