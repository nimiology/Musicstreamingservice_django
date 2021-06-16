from django.shortcuts import render
from .models import SingleTrack,Album
from .forms import SEARCH
# Create your views here.


#TODO: FRONT-END

def Search(request):
    if request.method == 'POST':
        TITLE = request.POST['Search']
        qssingletrack = SingleTrack.objects.filter(Title__contains=TITLE)
        qsalbum= Album.objects.filter(Title__contains=TITLE)
        context = {
            'Albumfound': qsalbum,
            'Singlefound':qssingletrack,
            'searchword':TITLE,
            'FORMS': SEARCH
        }
        return render(request,'Songs/Search.html',context)
    else:
        context = {
            'FORMS':SEARCH
        }
        return render(request,'Songs/Search.html',context)
#TODO: API
#TODO: COMMENTS
#TODO: SIGN UP
#TODO: SIGN IN

