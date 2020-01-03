from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),                                                  # Home page
    path('files', views.files, name = 'files'),                                         # For viewing all the files
    path('uploadFile', views.uploadFile, name='uploadFile'),                            # For uploading new files
    path('delete/<int:pk>', views.deleteFile, name='deleteFile'),                       # For deleting a file
    path('update/<int:pk>', views.updateFile, name='updateFile'),                       # For updating a file
    path('download/<int:pk>', views.downloadFile, name='downloadFile'),
]