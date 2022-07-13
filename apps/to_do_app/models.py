
from django.db import models

from typing import (
    List,
)
from django.contrib.auth.models import User 

from abstracts.models import(
    DateTimeCustom,
)

class Exercise(DateTimeCustom):

    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        verbose_name='Пользователь',
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True
    )
    activity = models.BooleanField(
        verbose_name='Активное задание',
        default=True
    )

    class Meta:
        ordering: List[str] = ['id',]
        verbose_name_plural: str = 'Задания'
        verbose_name: str = 'Задание'

    def __str__(self) -> str:
        return f'Задание для пользователя {self.user.username}'