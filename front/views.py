from django.http import  HttpResponse
from django.shortcuts import render,get_object_or_404
from  posts.models import  *
# Create your views here.

def frontpage(request):
    posts = Post.objects.filter(status=Post.ACTIVE)
    speakers = Speakers.objects.all()
    sponsors = Sponsors.objects.all()
    courses = Courses.objects.all()
    context = {'posts':posts,'speakers':speakers,'sponsors':sponsors,'courses':courses}
    return render(request, 'front/frontpage.html', context)
    
    
    
    
def about(request):
    return  render(request, 'front/about.html')
    
def signup(request):
    return  render(request, 'front/signup.html')
   
def robots_txt(request):
        text = [
        "User-Agent: *",
        "Disallow: /admin/",
        ]
        return HttpResponse("\n".join(text), content_type="text/plain")
   
