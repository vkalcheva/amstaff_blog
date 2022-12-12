from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('amstaff_blog.common.urls')),
    path('accounts/', include('amstaff_blog.accounts.urls')),
    path('dogs/', include('amstaff_blog.dogs.urls')),
    path('photos/', include('amstaff_blog.photos.urls')),
]
