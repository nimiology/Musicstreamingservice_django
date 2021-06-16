from django.shortcuts import render
from .models import SingleTrack,Album
# Create your views here.


#TODO: FRONT-END
#TODO:search part
def Search(request,TITLE):
    qsSingleTrack= SingleTrack.objects.filter(Title__contains=TITLE)
    print(qsSingleTrack)
    qsAlbum = Album.objects.filter(Title__contains=TITLE)
    print(qsAlbum)
    context = {
        'Singlefound': qsSingleTrack,
        'Albumfound': qsSingleTrack,
        'searchword': TITLE
    }
    render(request, 'Songs/Search.html', context)
#TODO: API
#TODO: COMMENTS
#TODO: SIGN UP
#TODO: SIGN IN

