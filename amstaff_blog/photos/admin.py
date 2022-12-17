from django.contrib import admin

from amstaff_blog.photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass

