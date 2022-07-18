import pytest

from django.urls import reverse

from core.models import Book
from core.serializers import BookSerializer


@pytest.mark.django_db
def test_list_book(client):
    username = 'test_erg'
    password = 'test_erg'
    url = reverse('core:books-list')
    books = Book.objects.all()
    expected_data = BookSerializer(books, many=True).data

    client.login(username=username, password=password)
    response = client.get(url)
    assert response.status_code == 200
    assert response.data == expected_data


@pytest.mark.django_db
def test_detail_book(client):
    username = 'test_erg'
    password = 'test_erg'
    url = reverse('core:books-detail', kwargs={'pk': 1})
    book = Book.objects.create(
        title='sample',
        publisher='sample'
    )
    expected_data = BookSerializer(book).data

    client.login(username=username, password=password)
    response = client.get(url)
    assert response.status_code == 200
    assert response.data == expected_data
