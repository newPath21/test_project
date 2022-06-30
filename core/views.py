from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from core.models import Book, TaggedItem
from core.serializers import BookSerializer, SuccessSerializer, TaggedItemCreateSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, ]


class TaggedItemCreateAPIView(APIView):
    @swagger_auto_schema(
        request_body=TaggedItemCreateSerializer(),
        responses={
            201: SuccessSerializer()
        }
    )
    def post(self, request, *args, **kwargs):
        tag_name = request.data['tag']
        TaggedItem.objects.create(tag=tag_name)
        return Response({'success': True})


class TaggedItemAPIView(APIView):
    def post(self, request, tag_id, book_id, *args, **kwargs):
        book = Book.objects.get(id=book_id)
        tag = TaggedItem.objects.get(id=tag_id)
        book.tags.add(tag)
        return Response({'success': True})
