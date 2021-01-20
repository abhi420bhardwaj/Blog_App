from django.urls import path , include
from .views import listUsers , listPosts , editPosts , createPosts , deletePosts

urlpatterns = [
    path('',listUsers,name = 'home'),
    path('<int:user_id>',listPosts , name = 'post'),
    path('<int:user_id>/<int:post_id>',editPosts , name = 'edit_post'),
    path('new/<int:user_id>',createPosts , name = 'create_post'),
    path('delete/<int:post_id>',deletePosts , name = 'delete_post'),
]
