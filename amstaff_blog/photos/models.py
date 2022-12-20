from django.core.validators import MinLengthValidator
from django.db import models

from amstaff_blog.dogs.models import Dog


class Photo(models.Model):
    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 300

    photo = models.URLField(
        null=False,
        blank=False,
    )

    description = models.CharField(
        # DB validation
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(
            # Django/python validation, not DB validation
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        ),
        null=True,
        blank=True,
    )
    location = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )

    publication_date = models.DateField(
        # Automatically sets current date on `save` (update or create)
        auto_now=True,
        null=False,
        blank=True,
    )

    dog = models.ForeignKey(
        Dog,
        on_delete=models.RESTRICT,
    )
