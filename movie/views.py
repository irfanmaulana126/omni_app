from .models import Movie
from django.template.loader import render_to_string
from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def MovieTemplate(request):
    return render(request,'index.html')

def MovieList(request):
    if request.POST and request.POST["search"] != "":
        movie_list = Movie.objects.filter(name__contains=request.POST["search"])
        print(movie_list)
        if movie_list.exists():
            list_movie = render_to_string('_list_movie.html', {
                        'arrs': movie_list,
            })
            result = True
            list_movie_html = list_movie
        else:
            result =  False
            list_movie_html = ''
        return JsonResponse({"result":result,"list_movie_html":list_movie_html})
    else :
        movie_list = Movie.objects.all()
        list_movie = render_to_string('_list_movie.html', {
                    'arrs': movie_list,
        })
        result = True
        list_movie_html = list_movie
        return JsonResponse({"result":result,"list_movie_html":list_movie_html})

def MovieDetail(request, pk):
    movie_detail = Movie.objects.get(pk=pk)
    return render(request,'movie_detail.html',{'movie':movie_detail})