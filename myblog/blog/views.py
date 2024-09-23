from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import PostSerializer
from django.utils.text import slugify


# GET ALL
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


#GET
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})


# POST
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(post.title)  
            while Post.objects.filter(slug=post.slug).exists():
                post.slug = f"{post.slug}-{Post.objects.filter(slug__startswith=post.slug).count() + 1}"
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

#PUT
def post_update(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_form.html', {'form': form})

#DELETE
def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    
    return render(request, 'blog/post_confirm_delete.html', {'post': post})


# API ViewSet
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)