from django.db import models



class Category (models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return  '/%s/' % self.slug 
class Post(models.Model):
    ACTIVE = 'active'
    DRAFT = 'draft'

    CHOICES_STATUS = (
        
        (ACTIVE, 'Active'),
        (DRAFT, 'Draft')
    
    )
    category = models.ForeignKey(Category, related_name='posts', default='All',on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    excerpt = models.TextField()
    body = models.TextField()
    date = models.DateTimeField( blank= True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)
    image = models.ImageField(upload_to='uploads/', blank= True, null=True)
    
    class  Meta:
        ordering = ('-created_at',)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return  '/%s/%s/' % (self.category.slug ,self.slug)
        
        
        
        
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    class  Meta:
        ordering = ('-created_at',)
    def __str__(self):
        return self.name
        
        
class Speakers(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField()
    expertise = models.CharField(max_length=255,null=True,blank=True)
    image = models.ImageField(upload_to='uploads/', blank= True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class  Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Speakers'
    def __str__(self):
        return self.name
        
        
        
class Sponsors(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/', blank= True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class  Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Sponsors'
    def __str__(self):
        return self.name

class Partners(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/', blank= True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class  Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Partners'
    def __str__(self):
        return self.name
        
class Courses(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField()
    image = models.ImageField(upload_to='uploads/', blank= True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class  Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Courses'
    def __str__(self):
        return self.name
    
    
    
