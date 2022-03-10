from django.urls import path
from . import views

app_name = 'Jobpost'

urlpatterns = [
    path('', views.JobView.as_view(), name = 'job'),
    path('<slug>/', views.JobDetailView.as_view(), name = 'JobDetail'),
]
