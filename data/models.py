from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from PIL import Image
from django.utils.text import Truncator




class Profile(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE ,related_name='Profile')
    name_f = models.CharField(max_length=200, null=True)
    name_l = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    img = models.ImageField(upload_to='images/%y/%m/%d', default='default/user3.png', blank=True, null=True)
    assistant = models.BooleanField(default=False, blank=True, null=True)
    admin = models.BooleanField(default=False, blank=True, null=True)
    
    def __str__(self):
        return f'{self.user}'
    
    @property
    def imgUser(self):
        if self.img is None:
            url = ''
        else:
            url = self.img.url
        return url
    
class Statistics(models.Model):
    views = models.IntegerField(default=0, null=True, blank=True)
    
    def __str__(self):
        return f'website visitors: {self.views}'
    
class Comment(models.Model):
    user = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE ,related_name='Comment')
    commet = models.TextField(max_length=500, null=True , blank=True)
    time = models.DateTimeField(default=datetime.now())
    best = models.BooleanField(default=False, null=True, blank=True)
    favourite = models.BooleanField(default=False, null=True, blank=True)
    
    def __str__(self):
        return f'{self.user}'
    
class UserMsg(models.Model):
    user = models.ForeignKey(Profile, null=True,blank=True, on_delete=models.CASCADE ,related_name='UserMsg')
    name_f = models.CharField(max_length=200, null=True)
    name_l = models.CharField(max_length=200, null=True)
    name_for_nonUser = models.CharField(max_length=300, blank=True, null=True)
    email = models.CharField(max_length=300, null=True, blank=True)
    msg = models.TextField(max_length=500, null=True, blank=True)
    time = models.DateTimeField(default=datetime.now())

    def __str__(self):
        if(self.name_f is not None and self.name_l is not None):
            return f'{self.name_f} {self.name_l} Message'
        else:
            return f'{self.name_for_nonUser} Message'
        
class About(models.Model):
    aboutS1 = models.TextField(max_length=1000, null=True, blank=True, default="Section_1")
    aboutS2 = models.TextField(max_length=1000, null=True, blank=True, default="Section_2")
    aboutS3 = models.TextField(max_length=1000, null=True, blank=True, default="Section_3")
    aboutS4 = models.TextField(max_length=1000, null=True, blank=True, default="Section_4")
    aboutSkills = models.TextField(max_length=1000, null=True, blank=True, default="Skills")
    
class Plog(models.Model):
    logo = models.CharField(max_length=100, null=True, blank=True, default="Logo")
    plogName = models.CharField(max_length=100, null=True, blank=True, default="Plog_Name")
    
    def __str__(self):
        return self.logo
    
class Project(models.Model):
    options = (
        ('Draft', 'Draft'),
        ('Published', 'Published'),
        ('Pnder update', 'Under Update'),
        ('Removed', 'Removed'),
    )
    
    name = models.CharField(max_length=200, null=True, blank=True, default='Project-Name')
    description = models.TextField(max_length=400, null=True, blank=True, default='Project-Description')
    status = models.CharField(max_length=20, choices=options, default='Draft') 
    created_dt = models.DateTimeField(default=datetime.now())
    github = models.URLField(blank=True,default='http://none.com', null=True)
    img = models.ImageField(upload_to='projects/%d', default="default/project.png", null=True, blank=True)
    link = models.CharField(max_length=300, null=True , blank=True, default="none")
    priority = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
def projectname(self, filename):
    return f'projects/images/{self.project.name}/{filename}'

class ProjectPhoto(models.Model):
    project = models.ForeignKey(Project,null=True, on_delete=models.CASCADE ,related_name='ProjectPhoto')
    img = models.ImageField(upload_to=projectname, default="default/project.png", null=True, blank=True)
    # img2 = models.ImageField(upload_to='projects/%d', default="default/project.png", null=True, blank=True)
    # img3 = models.ImageField(upload_to='projects/%d', default="default/project.png", null=True, blank=True)
    
    
    def __str__(self):
        return f'{self.project.name}-img'
    
class ProjectLanguage(models.Model):
    project = models.ForeignKey(Project,null=True, on_delete=models.CASCADE ,related_name='Language')
    name = models.CharField(max_length=100, default='unknown')
    img = models.ImageField(upload_to='projects/language/%d', null=True, blank=True)
    
    @property
    def langImg(self):
        if self.img is None:
            url = ''
        else:
            url = self.img.url
        return url
    
    def __str__(self):
        return f'{self.project.name}- {self.name} (language)'

    
    
class SocialLinks(models.Model):
    facebook = models.CharField(max_length=1000, null=True, blank=True)
    instagram = models.CharField(max_length=1000, null=True, blank=True)
    github = models.CharField(max_length=1000, null=True, blank=True)
    linkedin = models.CharField(max_length=1000, null=True, blank=True)
    watsapp = models.CharField(max_length=1000, null=True, blank=True)
    
class LastSearch(models.Model):
    content = models.TextField(max_length=500)
    user = models.ForeignKey(Profile, null=True, related_name='Profile', on_delete=models.CASCADE)
    search_dt = models.DateTimeField(default=datetime.now(), null=True, blank=True)

    def __str__(self):
        return f'{self.user.name_f} - {Truncator(self.content).chars(50)}'
    
class Code(models.Model):
    name = models.CharField(max_length=50)
    project = models.ForeignKey(Project,null=True, on_delete=models.CASCADE ,related_name='code')
    code_area = models.TextField(default='<span class="nocode">no data founded</span>')
    file_name = models.CharField(max_length=150, default='Untitled')
    
    def __str__(self):
        return f'{self.name} - {self.project.name}'