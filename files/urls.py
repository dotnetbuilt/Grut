from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.file_upload_view, name='upload'),
    path('list/', views.file_list_view, name='list'),
    path('download/<int:pk>/', views.file_download_view, name='download'),
]
