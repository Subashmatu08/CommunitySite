from web_site.utils import get_user_posts, is_friend
from django.contrib.auth.forms import UserCreationForm
from web_site import models
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import BlogForm, CodeGistForm, CreateUserForm, CustomAuthenticateForm, TweetCreationForm
from django.urls import reverse


ROOT_PAGE_NAME = "TheDumbCoder | "

# Create your views here.

def login_page(request):
    PAGENAME = ROOT_PAGE_NAME +'Login'
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CustomAuthenticateForm()
        if request.method == 'POST':
            form = CustomAuthenticateForm(request.POST)
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, "Username or Password is incorrect!!")
                return render(request, 'web_site/auth/login.html', {'form': form, 'page_name' : PAGENAME, })
        else:
            return render(request, 'web_site/auth/login.html', {'form': form, 'page_name' : PAGENAME, })

def register_page(request):
    PAGENAME = ROOT_PAGE_NAME + "Register"
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = CreateUserForm()
    return render(request, 'web_site/auth/register.html', {'form': form, "page_name" : PAGENAME})

@login_required(login_url="login")
def home(request):
    PAGE_NAME = ROOT_PAGE_NAME + "Home"
    posts = get_user_posts(request.user)
    form = TweetCreationForm()
    context = {
        "page_name" : PAGE_NAME,
        'posts' : posts,
        "user" : request.user,
        "users" : User.objects.all(),
        "form" : form
    }
    if request.method == 'POST':
        form = TweetCreationForm(request.POST)
        if form.is_valid():
            my_tweet = form.save(commit=False)
            post = models.Post.objects.create(posted_by=request.user, post_type="TWEET")
            my_tweet.post_ref = post
            my_tweet.save()
            return redirect('home')
        context["form"] = form
        return render(request, "web_site/home.html", context)
    return render(request, "web_site/home.html",  context)

@login_required(login_url="login")
def view_other_profile(request, username):
    user  =  User.objects.get(username=username)
    friend = is_friend(request.user, user)
    context = {
        'self' : request.user == user,
        'friend' : friend,
        'user' : user,
        'page_name' : ROOT_PAGE_NAME + " " + username
    }
    return render(request, "web_site/profile.html", context)


@login_required(login_url="login")
def profile_view(request):
    user = request.user
    blogs = []
    gists = []
    tweets = []
    posts = models.Post.objects.filter(posted_by=request.user)
    friend = is_friend(request.user, request.user)
    for post in posts:
        if post.post_type == "BLOG":
            blogs.append(models.Blog.objects.get(post_ref=post))
        elif post.post_type == "CODEGIST":
            gists.append(models.CodeGist.objects.get(post_ref=post))
        elif post.post_type == "TWEET" :
            tweets.append(models.Tweet.objects.get(post_ref=post))
    return render(request, "web_site/profile.html", {"self": True, "user" : user, "blogs" : blogs, "gists" : gists, "tweets" : tweets, "page_name" : ROOT_PAGE_NAME + " " + "Profile", "friend" : friend })


@login_required(login_url="login")
def feed_page(request, category_name):
    print(category_name)
    return render(request, "web_site/posts/posts.html", {"category_name" : category_name, "page_name" : ROOT_PAGE_NAME + category_name})

@login_required(login_url="login")
def blogs_page(request, category_name):
    category = models.Category.objects.get(category_name=category_name)
    posts = models.Post.objects.filter(category=category).filter(post_type="BLOG")
    blogs = []
    for post in posts:
        blog = models.Blog.objects.get(post_ref=post)
        blogs.append({
            "id" : blog.id,
            "author" : post.posted_by,
            "title" : blog.title,
            "description" : blog.description,
            "content" : blog.content,
        })
    return render(request, "web_site/posts/blogs_page.html", {'blogs' : blogs, "category_name" : category_name, "page_name" : category_name + " | " +"articles"})

@login_required(login_url="login")
def code_gists_page(request, category_name):
    category = models.Category.objects.get(category_name=category_name)
    posts = models.Post.objects.filter(category=category).filter(post_type="CODEGIST")
    code_gists = []
    for post in posts:
        code_gist = models.CodeGist.objects.get(post_ref=post)
        code_gists.append({
            "author" : post.posted_by,
            "code_snippet" : code_gist.code_snippet,
            "difficulty" : code_gist.difficulty,
            "language" : code_gist.language,
            "topic" : code_gist.topic,
            "id" : code_gist.id
        })
    return render(request, "web_site/posts/code_gists.html", {'code_gists' : code_gists, "category_name" : category_name, "page_name" : category_name + " | " + "gists"})

@login_required(login_url="login")
def create_blog(request):
    blog_form = BlogForm()
    if request.method == "POST":
        blog_form = BlogForm(request.POST)
        if blog_form.is_valid():
            post = models.Post.objects.create(post_type="BLOG", posted_by=request.user)
            my_blog = blog_form.save(commit=False)
            my_blog.post_ref = post
            my_blog.content = my_blog.content.lstrip()
            my_blog.save()
            return redirect(reverse('home'))
        return render(request, "web_site/posts/create_blog.html", {"form" : blog_form, "page_name" : ROOT_PAGE_NAME + " create blog"})
    return render(request, "web_site/posts/create_blog.html",  {"form" : blog_form, "page_name" : ROOT_PAGE_NAME + " create blog"})
    
@login_required(login_url="login")
def create_code_gist(request):
    gist_form = CodeGistForm()
    if request.method == "POST":
        gist_form = CodeGistForm(request.POST)
        if gist_form.is_valid() :
            post = models.Post.objects.create(post_type="CODEGIST", posted_by=request.user)
            code_gist = gist_form.save(commit=False)
            code_gist.post_ref = post
            code_gist.save()
            return redirect(reverse('home'))    
        return render(request, "web_site/posts/create_code_gist.html", {"form" : gist_form, "page_name" : ROOT_PAGE_NAME + " create gist"})
    return render(request, "web_site/posts/create_code_gist.html", {"form" : gist_form, "page_name" : ROOT_PAGE_NAME + " create gist"})


def view_blog(request, blog_id):
    blog = models.Blog.objects.get(id=blog_id)
    return render(request, "web_site/posts/view_blog.html", {"content" : blog, "page_name" : blog.title})

def view_code_gist(request, code_gist_id):
    code_gist = models.CodeGist.objects.get(id=code_gist_id)
    return render(request, "web_site/posts/view_code_gist.html", {"content" : code_gist, "page_name" : ROOT_PAGE_NAME})


def logout_view(request):
    logout(request)
    return redirect("login")