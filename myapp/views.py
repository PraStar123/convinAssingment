from django.shortcuts import render, redirect
from .models import FileModel
from .forms import FileForm, FileUpdateForm
from django.contrib import messages
from django.http import Http404, HttpResponse
from django.conf import settings
from .serializers import FileSerializer, OperationSerializer
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework import generics, status 
from rest_framework import viewsets
import os 



# Create your views here.
# Home Page views
def home(request):
    return redirect('files')

# For viewing all the files in database
def files(request):
    files = FileModel.objects.all()
    args = {
        'files' : files
    }
    return render(request, "files.html", args)

# For uploading a file
def uploadFile(request):
    if request.POST:
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, f"File '{request.POST['fileName']}' has been uploaded")
            return redirect('files')
    else:
        form = FileForm()
    
    args = {
        'form' : form
    }

    return render(request, 'upload_2.html', args)

# For updating existing file
def updateFile(request, pk):
    instance = FileModel.objects.get(pk=pk)
    if request.POST:
        prevFile = instance.tracker.previous('fileName')
        prevFilePath = instance.tracker.previous('filePath')
        form = FileUpdateForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if prevFile != instance.fileName:
                messages.info(request, f"File name has been changed from '{prevFile}' to '{instance.fileName}'")
            if prevFilePath != instance.filePath:
                messages.info(request, f"File content changed from '{prevFilePath}' to '{instance.filePath}'")
            return redirect('files')
    else:
        form = FileUpdateForm(instance=instance)
    args = {
        'form': form
    }
    return render(request, "update.html", args)

# For deleting existing file
def deleteFile(request, pk):
    file = FileModel.objects.get(pk=pk)
    if file:
        messages.info(request, f"'{file.fileName}' has been deleted")
        file.delete()
    return redirect('files')

# For downloading a file
def downloadFile(request, pk):
    file = FileModel.objects.get(pk=pk)
    if file: 
        givenPath = os.path.join(settings.MEDIA_ROOT, file.filePath.path)
        if os.path.exists(givenPath):
            with open(givenPath, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/text")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(givenPath)
                return response
    else: 
        raise Http404
    return redirect('files')

# For uploading file via REST api
class FileViewSet(viewsets.ModelViewSet):
    queryset = FileModel.objects.all()
    serializer_class = FileSerializer
   










