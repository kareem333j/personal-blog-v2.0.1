from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *

import random
from django.utils.text import Truncator

# django models functions
from django.db.models import Q
from django.db.models import Value
from django.db.models.functions import Concat
# pagination
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def unauthenticated_user(view_func):
    def warpper_func(request, *args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args,**kwargs)

    return warpper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def warpper_func(request, *args,**kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args,**kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return warpper_func
    return decorator

def search_page(request, page_number, shuffle):
    search_content = str(request.GET.get('s'))
    
    if request.user.is_authenticated:
        if not LastSearch.objects.filter(Q(user=request.user.Profile) & Q(content = search_content)):
            LastSearch.objects.create(
                user = request.user.Profile,
                content = search_content
            )
        
    comments = Comment.objects.annotate(full_name=Concat('user__name_f',Value(' '),'user__name_l')).filter(
        Q(commet__icontains = search_content) |
        Q(full_name__icontains = search_content) 
    )
    
    profiles = Profile.objects.annotate(full_name=Concat('name_f',Value(' '),'name_l')).filter(
        Q(full_name__contains=search_content) |
        Q(user__username__contains=search_content) |
        Q(pk__contains=search_content) 
    )
    
    projects = Project.objects.filter(
        Q(name__contains=search_content) |
        Q(description__contains=search_content) 
    )
    
    results_list = []
    
    for user in profiles:
        object = {
            'id': user.user_id,
            'full_name': Truncator(user.full_name).chars(40),
            'username': user.user.username,
            'img': user.imgUser,
            'type': 'user',
            'data_joined': user.user.date_joined,
            'super_user': user.admin
        }
        results_list.append(object)
        
    for comment in comments:
        object = {
            'id': comment.id,
            'user_id': comment.user.user_id,
            'full_name': Truncator((comment.user.name_f+' '+comment.user.name_l)).chars(40),
            'username': comment.user.user.username,
            'comment': Truncator(comment.commet).chars(60),
            'created_dt': comment.time,
            'type': 'comment'
        }
        results_list.append(object)
        
    for project in projects:
        object = {
            'id': project.id,
            'full_name': Truncator(project.name).chars(40),
            'description': Truncator(project.description).chars(160),
            'type': 'project'
        }
        results_list.append(object)
        
    if shuffle == True:
        results_list_shuffled = sorted(results_list, key=lambda x: random.random())
    else:
        results_list_shuffled = results_list
    
    paginator = Paginator(results_list_shuffled, 7)
    page = page_number
    try:
        results_list_shuffled = paginator.page(page)
    except PageNotAnInteger:
        return render(request, '404.html',status=404)
    except EmptyPage:
        results_list_shuffled = paginator.page(paginator.num_pages)
    
    pages_number = paginator.page_range
    pagination_in_first = False
    pagination_in_last = False
    pagination_in_mid = False
    if paginator.num_pages > 7 and page < 6:
        pages_number = paginator.page_range[:6]
        pagination_in_first = True
    elif paginator.num_pages > 7 and (page >= 6 and page < paginator.num_pages - 4):
        pages_number = paginator.page_range[page-3:page+2]
        pagination_in_mid = True
    elif paginator.num_pages > 7 and page > paginator.num_pages - 5:
        pages_number = paginator.page_range[paginator.num_pages-6:paginator.num_pages]
        pagination_in_last = True
    else:
        pages_number = paginator.page_range
    
    context = {
        'search_content': search_content,
        'results': results_list_shuffled,
        'paginator': paginator,
        'blog':Plog.objects.all(),
        'social': SocialLinks.objects.all(),
        'pages_number': pages_number,
        'page_number': page,
        'pagination_in_first': pagination_in_first,
        'pagination_in_mid': pagination_in_mid,
        'pagination_in_last': pagination_in_last
    }
    
    return context

