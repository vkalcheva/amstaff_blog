from django.shortcuts import render


def add_dog(request):
    return render(request, 'dogs/pet-add-page.html')


def delete_dog(request):
    return render(request, 'dogs/pet-delete-page.html')


def details_dog(request):
    return render(request, 'dogs/pet-details-page.html')


def edit_dog(request):
    return render(request, 'dogs/pet-edit-page.html')

