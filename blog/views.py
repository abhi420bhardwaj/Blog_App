from django.shortcuts import render , redirect
from .models import User,Post
from .forms import PostForm

# Create your views here.

def listUsers(request):

    user = User.objects.all()
    return render(request,'home.html',{'users':user})

def listPosts(request,user_id):
    post = Post.objects.filter(author = user_id )
    user = User.objects.get(id=user_id)
    return render(request,'post.html',{'posts':post,'user':user})

def editPosts(request,user_id,post_id):

    form = PostForm(request.POST)
    if form.is_valid():
        edited_post = form.save(commit=False)
        edited_post.author = User.objects.get(id = user_id )
        edited_post.id = post_id
        edited_post.save()
        return redirect('post',user_id=user_id)


    return render(request , 'edit_post.html',{'form':form})

def createPosts(request,user_id):

    form = PostForm(request.POST)
    if form.is_valid():
        new_post = form.save(commit=False)
        new_post.author = User.objects.get(id = user_id )
        new_post.save()
        return redirect('post',user_id=user_id)


    return render(request , 'edit_post.html',{'form':form})

def deletePosts(request,user_id , post_id):
    deleting_post = Post.objects.get(id=post_id)
    if request.method == "POST":
        deleting_post.delete()
        return redirect('post',user_id=user_id)
    return render(request , 'post_confirm_delete.html',{})
