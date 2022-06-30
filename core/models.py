from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from .abstarct import AbstractDateTime
from django.utils.translation import ugettext_lazy as _


class Book(AbstractDateTime):
    title = models.CharField(
        _('название'),
        max_length=126
    )
    publisher = models.CharField(
        _('издатель'),
        max_length=126
    )
    author = models.CharField(
        _('автор'),
        max_length=126,
        blank=True,
        null=True
    )
    pages = models.PositiveSmallIntegerField(
        _('страницы'),
    )
    tags = GenericRelation('TaggedItem')


class TaggedItem(models.Model):
    tag = models.CharField(
        _('tag'),
        max_length=126
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.tag

    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]
