from django.shortcuts import render, get_object_or_404
from .models import Post
from django import forms


def home(request):
    return render(request, 'blog/index.html')

def blog(request):
    return render(request, 'blog/blog.html')
    
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

def details_posts(request, id):
    post = get_object_or_404(Post, id=id)  
    return render(request, 'blog/posts_detail.html', {'post': post})

class PostForm(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.CharField(widget=forms.Textarea)

def form_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()  
            Post.objects.create(
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content']
            )
            return redirect('post_list') 
    else:
        form = PostForm()
    
    return render(request, 'blog/formulaire_post.html', {'form': form})
