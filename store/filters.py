import django_filters
from .models import Book


class SnippetFiler(django_filters.FilterSet):

    class Meta:
        model = Book
        fields = ('title', 'author', 'price')
