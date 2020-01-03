from django.urls import path 
from . import views

urlpatterns = [
    path('files', views.files, name = 'files'),                     # For viewing all the files
    path('uploadFile', views.uploadFile, name='uploadFile'),        # For uploading new files
    path('delete/<int:pk>', views.deleteFile, name='deleteFile'),   # For deleting a file
    path('update/<int:pk>', views.updateFile, name='updateFile'),   # FOr updating a file
]