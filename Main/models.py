from django.db import models

# Create your models here.


class WallpaperIMg(models.Model):
     wallpaperName = models.CharField(max_length=100)
     wallpaperImg = models.ImageField(upload_to='Wallpapers')


     def __str__(self):
          return self.wallpaperName
     

class feedback_msg(models.Model):
     datatime = models.DateTimeField(auto_now_add=True)
     first_name = models.CharField(max_length=100)
     last_name = models.CharField(max_length=100)
     country = models.CharField(max_length=20)
     msg = models.TextField()


     def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}{self.datatime}'
     