from django.urls import path, include

from amstaff_blog.dogs.views import add_dog, details_dog, edit_dog, delete_dog

urlpatterns = (
    path('add/', add_dog, name='add dog'),
    path('<str:username>/dog/<slug:dog_name>/', include([
        path('', details_dog, name='details dog'),
        path('edit/', edit_dog, name='edit dog'),
        path('delete/', delete_dog, name='delete dog'),

    ]))
)