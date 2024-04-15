from django.contrib import admin
from django.contrib.admin import ModelAdmin
from movie.models import *

# Register your models here.
@admin.register(Movie)
class MovieAdmin(ModelAdmin):
    list_display=('name','description','imagePath','duration','get_genre','language','mpaaRating','userRating')

    def get_genre(self, obj):
        return ", ".join([g.name_genre for g in obj.genre.all()])

@admin.register(Genre)
class GenreAdmin(ModelAdmin):
    list_display=('name_genre',)

@admin.register(MpaaRating)
class MpaaRatingAdmin(ModelAdmin):
    list_display = ('label','type')