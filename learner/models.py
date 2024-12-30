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
#new model
class Progress(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # Ensure 'auth.User' is correct
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE, default=1)

    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.lesson.title} - {'Completed' if self.completed else 'Incomplete'}"



class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.IntegerField(help_text="Duration in minutes")

    def __str__(self):
        return self.title

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=200)
    content = models.TextField()
    order = models.IntegerField()
    

    def __str__(self):
        return f"{self.course.title} - {self.title}"

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_on = models.DateTimeField(auto_now_add=True)


