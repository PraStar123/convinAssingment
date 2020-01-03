from django.db import models
from time import time
from django.dispatch import receiver
from django.db.models.signals import post_save
from model_utils import FieldTracker
from cryptography.fernet import Fernet
from django.conf import settings
import os


# Create your models here.

#def my_file_name(instance, filename):
#    return "uploaded_files/%s_%s" % (str(time).replace('.','-'), filename)

# My file model
class FileModel(models.Model):
    fileName = models.CharField(max_length=256)
    filePath = models.FileField(upload_to='files')
    tracker = FieldTracker()
    encryption = models.CharField(max_length=1024,blank=True)
    
    def __unicode__(self):
        return self.fileName
    
    def delete(self, *args, **kwargs):
        self.filePath.delete()
        self.fileName = None
        super().delete(*args, **kwargs)

# Encryption using Fernet keys
@receiver(post_save, sender=FileModel)
def trackCreated(sender, instance, created, **kwargs):
    if created:
        current = FileModel.objects.get(pk=instance.id)
        with open(os.path.join(settings.BASE_DIR, f"media/{current.filePath}"), 'rb') as f:
            contents = f.read()
            key = Fernet.generate_key()
            fernet = Fernet(key)
            encrypted = fernet.encrypt(contents)            
            current.encryption = encrypted.decode('ascii')
            current.save()


post_save.connect(trackCreated, sender=FileModel)

