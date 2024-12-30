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
   
    path('module/<int:module_id>/', views.view_module, name='view_module'),
    path('complete-module/<int:module_id>/', views.complete_module, name='complete_module'),
    path('dashboard/', views.student_dashboard, name='student_dashboard'),

    path('', views.CourseListView.as_view(), name='course-list'),
    path('course/<int:pk>/', views.CourseDetailView.as_view(), name='course-detail'),
    path('enroll/<int:course_id>/', views.enroll, name='enroll'),
    path('progress/', views.progress, name='progress'),
]
