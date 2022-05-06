from django.urls import path
from .  import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('<slug:category_slug>/<slug:slug>/', views.detail, name='post_detail'),
    path('speakers/', views.speakers, name='speakers'),
    path('courses/', views.courses, name='courses'),
    path('sponsors/', views.sponsors, name='sponsors'),
    path('partners/', views.partners, name='partners'),
    path('<slug:slug>/', views.category, name='category_detail')
    
        ]
    