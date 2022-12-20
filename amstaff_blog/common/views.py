from django.shortcuts import render

from amstaff_blog.photos.models import Photo


def index(request):
    context = {
        'photos': Photo.objects.all(),
    }
    return render(request, 'common/home-page.html', context)
