from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from .models import  *
from .forms import *


def detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug, status= Post.ACTIVE)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return  redirect ('post_detail', slug=slug,category_slug=category_slug)
    else:
        form = CommentForm()
    speakers = Speakers.objects.all()
    sponsors = Sponsors.objects.all()
    partners = Partners.objects.all()
    courses = Courses.objects.all()
    context = {'post' : post , 'form':form,'speakers':speakers,'sponsors':sponsors,'courses':courses,'partners':partners}
    return  render(request, 'posts/detail.html', context)
    
    
    
def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=Post.ACTIVE)
    speakers = Speakers.objects.all()
    sponsors = Sponsors.objects.all()
    partners = Partners.objects.all()
    courses = Courses.objects.all()
    
    context={'category':category,'posts':posts,'speakers':speakers,'sponsors':sponsors,'courses':courses,'partners':partners}
    
    return render(request, 'posts/category.html', context)
    
    
def speakers(request):
    speakers = Speakers.objects.all()
    sponsors = Sponsors.objects.all()
    partners = Partners.objects.all()
    courses = Courses.objects.all()
    context = {'speakers':speakers,'sponsors':sponsors,'courses':courses,'partners':partners}
    return  render(request, 'posts/speakers.html', context)
    
def sponsors(request):
    speakers = Speakers.objects.all()
    sponsors = Sponsors.objects.all()
    partners = Partners.objects.all()
    courses = Courses.objects.all()
    context = {'speakers':speakers,'sponsors':sponsors,'courses':courses,'partners':partners}
    return  render(request, 'posts/sponsors.html', context)
    
    
def partners(request):
    speakers = Speakers.objects.all()
    sponsors = Sponsors.objects.all()
    partners = Partners.objects.all()
    courses = Courses.objects.all()
    context = {'speakers':speakers,'sponsors':sponsors,'courses':courses,'partners':partners}
    return  render(request, 'posts/partners.html', context)
 
def courses(request):
    speakers = Speakers.objects.all()
    sponsors = Sponsors.objects.all()
    partners = Partners.objects.all()
    courses = Courses.objects.all()
    context = {'speakers':speakers,'sponsors':sponsors,'courses':courses,'partners':partners}
    return  render(request, 'posts/courses.html', context)
    
def search(request):
    query = request.GET.get('query', '')
    posts = Post.objects.filter(status=Post.ACTIVE).filter(Q(title__icontains=query) | Q(excerpt__icontains=query) | Q(body__icontains=query))
    speakers = Speakers.objects.all()
    sponsors = Sponsors.objects.all()
    partners = Partners.objects.all()
    courses = Courses.objects.all()
    context = {'posts': posts, 'query': query,'speakers':speakers,'sponsors':sponsors,'courses':courses,'partners':partners}
    return  render(request, 'posts/search.html', context)
    
