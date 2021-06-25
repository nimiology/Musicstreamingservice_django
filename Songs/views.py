from django.shortcuts import render,get_object_or_404
from .models import SingleTrack,Album,Playlist
from .forms import SEARCH




def SINGLETRACK(request,Slug):
    SINGLETRACK = get_object_or_404(SingleTrack,Slug=Slug)
    context = {
        'Single':SINGLETRACK
    }
    return render(request,'Songs/SingleTrack.html',context)

def ALBUM(request,Slug):
    Albums = get_object_or_404(Album,Slug=Slug)
    singletrack_list = Albums.SingleTrack.all()
    context = {
        'Singles': singletrack_list,
        'Album':Albums
    }

    return render(request, 'Songs/Album.html', context)

#todo: playlist
#SEARCH
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
