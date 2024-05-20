from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('post/new/', views.PostCreateView.as_view(), name='create'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='edit'),
]