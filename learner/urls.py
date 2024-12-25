from django.urls import path
from .views import login_view
from .views import signup_view

from . import views


urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path("index/", views.index, name="index"),
    path("welcome/",views.welcome, name="welcome"),
    path("logout",views.logout_view, name="logout"),
   # path('accounts/', include('allauth.urls')),  # Allauth URLs
    path('module/<int:module_id>/', views.view_module, name='view_module'),
    path('complete-module/<int:module_id>/', views.complete_module, name='complete_module'),
    path('dashboard/', views.student_dashboard, name='student_dashboard'),




]
