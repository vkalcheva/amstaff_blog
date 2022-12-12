from django.urls import path

from amstaff_blog.common.views import index

urlpatterns = (
    path('', index, name='index'),
)