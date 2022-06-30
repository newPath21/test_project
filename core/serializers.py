from abc import ABC

from rest_framework import serializers
from .models import Book, TaggedItem


class ItemRelatedField(serializers.RelatedField, ABC):
    def to_representation(self, value):
        return TaggedItemCreateSerializer(value).data['tag']


class BookSerializer(serializers.ModelSerializer):
    tags = ItemRelatedField(read_only=True, many=True)

    class Meta:
        model = Book
        fields = [
            'id',
            'created_at',
            'updated_at',
            'title',
            'publisher',
            'author',
            'pages',
            'tags'
        ]


class SuccessSerializer(serializers.Serializer):
    success = serializers.BooleanField()


class TaggedItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaggedItem
        fields = [
            'tag'
        ]
