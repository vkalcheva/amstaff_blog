from django.urls import path, include

from amstaff_blog.dogs.views import add_dog

urlpatterns = (
    path('add/', add_dog, name='add dog'),
    path('<str:username>/dog/<slug:dog_name/', include([

    ]))
)