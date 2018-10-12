from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.utils import timezone
from .models import Post, Category
from .forms import PostForm
from django.contrib.auth import login, authenticate
#from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm

def handler404(request):
    return render(request, 'blog/404.html', status=404)

def handler500(request):
    return render(request, 'blog/500.html', status=500)

    
def post_list(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 5) # Show 5 contacts per page
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/post_list.html', {'posts': posts})
    
    
def post_category_wise(request, slug):
    category = get_object_or_404(Category, slug=slug)
    post_list = Post.objects.filter(category=category)
    paginator = Paginator(post_list, 5) # Show 5 contacts per page

    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail1(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_detail2(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})
		
def post_add(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                #return redirect('post_detail1', pk=post.pk)
                return redirect('post_list')
                #return redirect('post_detail2', slug=post.slug)
        else:
            form = PostForm()
        return render(request, 'blog/post_add.html', {'form': form})
    else:
        return redirect('post_list')
		
def post_edit1(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('post_detail1', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})
    else:
        return redirect('post_list')

        
def post_edit2(request, slug):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, slug=slug)
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('post_detail2', slug=post.slug)
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})
    else:
        return redirect('post_list')
        
def profile(request):
    return render(request, 'registration/profile.html')

def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration.html', {'form': form})