from django.db import models
import uuid

class DateTimeCustom(models.Model):
    id = models.UUIDField(
        primary_key= True,
        default=uuid.uuid4,
        editable = False,
        verbose_name='Идетификатор',
    )

    date_time_created = models.DateTimeField(
        auto_now_add = True,
        verbose_name = "Дата и время создания",
    )
    date_time_deleted = models.DateTimeField(
        verbose_name='Дата и время удоления',
        null = True,
        blank = True,
    )
    existanse_duration = models.DurationField(
        verbose_name='Время существования',
        null = True,
        blank = True,
    )

    class Meta:
        abstract = True

