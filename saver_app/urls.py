from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_page, name="home-page"),
    # user account
    path('register/', views.register_page, name="register-page"),
    path('login/', views.login_page, name="login-page"),
    path('logged_out/', views.logged_out_page, name="logged_out-page"),
    path('all_pws/', views.user_pw_all, name="all-page"),
    path('add_pw/', views.user_pw_add, name="add-page"),
    path('search_pw/', views.user_pw_search, name="search-page"),
    path('edit/<str:pk>/', views.edit_post, name="edit"),
    path('delete/<str:pk>/', views.delete, name="delete"), 
]