"""students_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from students.templates.views import students_views, groups_views


urlpatterns = [
    # Students urls
    path('', students_views.students_list, name='home'),
    path('students/add/', students_views.students_add, name='students_add'),
    path('students/<int:sid>/edit/', students_views.students_edit, name='students_edit'),
    path('students/<int:sid>/delete/', students_views.students_delete, name='students_delete'),

    # Groups urls
    path('groups/', groups_views.groups_list, name='groups'),
    path('groups/add/', groups_views.groups_add, name='groups_add'),
    path('groups/<int:gid>/edit/', groups_views.groups_edit, name='groups_edit'),
    path('groups/<int:gid>/delete/', groups_views.groups_delete, name='groups_delete'),

    # Admin
    path('admin/', admin.site.urls),
]
