from django.db import models

# Create your models here.

class Profile(models.Model):
  name = models.CharField(max_length=128)
  about = models.CharField(max_length=256)
  

  def __str__(self):
        return self.name

class Projects(models.Model):
  name = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile')
  title = models.CharField(max_length=128)
  image = models.ImageField(blank=True, upload_to='blog_images')


  def __str__(self):
        return self.title



