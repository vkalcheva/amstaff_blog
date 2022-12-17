from django.contrib import admin

from amstaff_blog.dogs.models import Dog


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    pass
