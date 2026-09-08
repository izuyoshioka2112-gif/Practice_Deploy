from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name="login.html"),
        name="login"), 
    path('book/index', views.index_view, name='index'),
    path('book/', views.ListBookView.as_view(), name='list-book'),
    path('book/<int:pk>/detail/', views.DetailBookView.as_view(), name='detail-book'),
    path('book/create/', views.CreateBookView.as_view(), name='create-book'),
    path('book/<int:pk>/delete/', views.DeleteBookView.as_view(), name='delete-book'),
    path('book/<int:pk>/update/', views.UpdateBookView.as_view(), name='update-book'),
    
]
