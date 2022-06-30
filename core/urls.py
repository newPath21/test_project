from django.urls import path, include
from . import views
from rest_framework import routers

from .views import TaggedItemAPIView, TaggedItemCreateAPIView

router = routers.DefaultRouter()
router.register('books', views.BookViewSet)

app_name = 'core'
urlpatterns = [
    path('', include(router.urls)),
    path('tags/<str:tag_id>/books/<str:book_id>', TaggedItemAPIView.as_view()),
    path('tags/', TaggedItemCreateAPIView.as_view())

]
