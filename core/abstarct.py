from django.db import models
from django.utils.translation import ugettext_lazy as _


class AbstractDateTime(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Дата создания')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Дата изменения')
    )