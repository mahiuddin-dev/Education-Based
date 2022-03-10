from django.urls import path
from . import views

app_name = 'Blog'

urlpatterns = [
    path('', views.BlogView.as_view(), name = 'Blog'),
    # path('<slug>/', views.BlogDetails, name = 'BlogDetail'),
    path('<slug>/', views.BlogDetailView.as_view(), name = 'BlogDetail'),
    # path('category/<slug>/', views.CategoryView, name = 'Category'),
    path('category/<slug>/', views.CategoryView2.as_view(), name = 'Category'),
    path('manik', views.new, name = 'chk'),
]
