from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'movies': ['Highlander', 'Stargate', 'Infinity War']
    }
    return render(request, 'movies/index.html', context)


# Structure for templates:
# appname/templates/appname/index.html
# eg. movies/templates/movies/index.html

def about(request):
    return render(request, 'movies/about.html', {})
