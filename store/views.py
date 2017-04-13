from django.shortcuts import render
from .models import Book

# Create your views here.
def index(request):
      return render(request,'template.html')

def store(request):
    count = Book.objects.all().count()
    context = {'count': count,
               }

    request.session['location'] = "NO SE SABE"
    if request.user.is_authenticated():
        request.session['location'] = "la TIERRA"

    return render(request, 'store.html', context)

    #version_anterio return render(request, 'store.html')