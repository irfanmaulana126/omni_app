from django.db import models

# Create your models here.

class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name_genre = models.CharField(max_length=64,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name_genre

class MpaaRating(models.Model):
    type = models.CharField(max_length=10,null=True)
    label = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.type+' - '+self.label

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    description=models.TextField(blank=True, null=True)
    imagePath=models.ImageField(upload_to='assets/images/', blank=True, null=True)
    duration=models.IntegerField(default=0)
    genre=models.ManyToManyField(Genre)
    language=models.CharField(max_length=100, blank=True, null=True)
    mpaaRating=models.ForeignKey(to='MpaaRating', on_delete=models.SET_NULL,related_name='mpaaRating',null=True,blank=True)
    userRating=models.CharField(max_length=10,default='0',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)
