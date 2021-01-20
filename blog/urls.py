from django.urls import path , include
from .views import listUsers , listPosts , editPosts , createPosts , deletePosts

urlpatterns = [
    path('',listUsers,name = 'home'),
    path('users',listUsers,name = 'home'),
    path('user/<int:user_id>',listPosts , name = 'post'),
    path('user/<int:user_id>/post/<int:post_id>/edit',editPosts , name = 'edit_post'),
    path('user/<int:user_id>/new',createPosts , name = 'create_post'),
    path('user/<int:user_id>/post/<int:post_id>/delete',deletePosts , name = 'delete_post'),
]
