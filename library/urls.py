"""library URL Configuration

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
from app import views

# from app.views import admin_view, librarian_view, student_view

urlpatterns = [
    path('admin1/', admin.site.urls),
    path('student_registation', views.register),
    path('', views.admin_register),
    path('home',views.home),
    path('admin',views.admin),
    path('login', views.user_login),
    path('logout',views.logout),
    path('add_book',views.add_book),
    path('booklist',views.book_list),
    path('transaction',views.take_book),
    path('transa_book',views.transaction_book_list),
    path('book_return',views.return_book),
    path('return_book_list',views.return_book_list),
    path('course_add',views.course_details_forms),
    path('course_details_history',views.course_details_history),
    path('admin_register_history',views.admin_register_history),
    path('student_register_history',views.student_register_history,name="student_register_history"),
    # path('student_fee',views.student_fee),
    # path('student_showing_fee',views.student_showing_fee),
    

    
]