"""base_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from .views import home_page, organization_list, project_list, all_organizations
from project_app.urls import urlpatterns as project_app_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('organizations/', organization_list, name='organizations'),
    path('projects/', project_list, name='projects'),
    path('api/organizations/', all_organizations, name='api_organizations'),
]

# Add other apps url to the base app
urlpatterns += project_app_urls

admin.site.index_title = "Seedcase Portal Administration"
admin.site.site_header = "Seedcase Portal Administration"
admin.site.site_title = "Seedcase Portal Administration"
