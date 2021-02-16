from django.urls import path,include
from basic_app import views

#Template Urls
app_name = 'basic_app'

urlpatterns = [
    path('register/', views.Register_page, name='Register_page'),
    path('user_login/', views.user_login, name='user_login'),
]
