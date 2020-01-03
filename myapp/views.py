from django.shortcuts import render, redirect
from .models import FileModel
from .forms import FileForm, FileUpdateForm
from django.contrib import messages

# Create your views here.

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








