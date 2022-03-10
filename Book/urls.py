from django.urls import path
from . import views

app_name = 'Book'

urlpatterns = [
    path('', views.HomeView.as_view(), name = 'book'),
    path('<slug>/', views.BookDetailView.as_view(), name = 'BookDetail'),
]
