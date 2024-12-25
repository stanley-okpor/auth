from django.db import models
from django.contrib.auth.models import User



#class User(AbstractUser):
  # is_student = models.BooleanField(default=True)
  #  pass

class Module(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()  # You can use rich text editors like CKEditor
    created_at = models.DateTimeField(auto_now_add=True)

class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    last_accessed = models.DateTimeField(auto_now=True)
