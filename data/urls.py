from django.urls import path
from . import views
urlpatterns = [
    path('',views.home , name='home'),
    path('dashboard',views.dashboard , name='dashboard'),
    path('project/<int:pk>',views.project , name='project'),
    path('profile/<str:pk>/', views.userProfile , name='userProfile'),
    path('editUser/<str:pk>/',views.editUser , name='editUser'),
    path('view_project/', views.project_view, name='view_project'),
    path('edit-project/<str:pk>/', views.edit_project, name='edit-project'),
    path('add-project', views.addProject, name="add-project"),
    path('search_result/', views.search, name='search'),
    path('search_result/page/<int:pk>', views.search_current_page, name='search_page'),
    path('search_suggestions/', views.getSuggestions, name='search_suggestions'),
    path('delete_suggestion/', views.delete_suggestion, name='delete_suggestion'),
    
    # auth
    path('login',views.userLogin , name='login'),
    path('register',views.register , name='register'),
    path('logout',views.userLogout , name='logout'),
]