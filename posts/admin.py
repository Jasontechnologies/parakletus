from django.contrib import admin

# Register your models here.
from  .models import  *


class CommentItemInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ['post']


class PostAdmin(admin.ModelAdmin):
    search_fields = ['title','excerpt','body']
    list_display = ['title','category','created_at','status']
    list_filter = ['category','created_at','status']
    inlines = [CommentItemInline]
    prepopulated_fields = {'slug':('title',),'excerpt':('body',)}
    
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'created_at']
    
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']
    prepopulated_fields = {'slug':('title',)}
    
class SpeakersAdmin(admin.ModelAdmin):
    list_display = ['name', 'expertise', 'age']
    search_fields = ['name']
    list_display = ['name']
class SponsorsAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_display = ['name']
    
class CoursesAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_display = ['name']
   

class PartnersAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_display = ['name'] 
    
    
admin.site.register(Post,PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin )
admin.site.register(Speakers, SpeakersAdmin)
admin.site.register(Sponsors, SponsorsAdmin)
admin.site.register(Courses, CoursesAdmin)
admin.site.register(Partners, PartnersAdmin)