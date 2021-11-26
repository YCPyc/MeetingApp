"""sbcodes URL Configuration

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
from django.urls import path, include 
from meeting.views import frontPage, postDetail, addPage, updatePage, deletePage, videologin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('topics/<int:pk>/',postDetail,name='postDetail'),
    path('', include('meeting.urls')),
    # have to put this upfront
    path('add/',addPage.as_view(),name='addPage'),
    path('topics/update/<int:pk>',updatePage.as_view(),name='updatePage'),
    path('topics/<int:pk>/delete',deletePage.as_view(),name='deletePage'),
    path('',frontPage,name='frontPage'),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
