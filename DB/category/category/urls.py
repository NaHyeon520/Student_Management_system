"""category URL Configuration

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

from django.urls import path
from myApp import views  # 그냥 myApp하면 연결은 됨. 아무것도 안뜸

urlpatterns = [
    path('', views.display, name='index'),
    path('add', views.add, name='add'),
    path('update/<int:stud_id>', views.update, name='update'),
    path('<int:stud_id>', views.delete, name='delete')
]

