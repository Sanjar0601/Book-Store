from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Book
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    View
)
from .filters import SnippetFiler
# Create your views here.


class BookListView(ListView):
    model = Book
    template_name = 'store/home.html'
    context_object_name = 'books'




class SearchView(ListView):
    model = Book
    template_name = 'store/snippet_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['filter'] = SnippetFiler(self.request.GET, queryset=self.get_queryset())
        return context



class BookDetailView(DetailView):
    model = Book
    template_name = 'store/book_detail.html'


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'summary', 'price', 'cover']


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'summary', 'price', 'cover']

    def test_func(self):
        users = self.get_object()
        if self.request.user == users:
            return True
        return False


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False






def home(request):
    return render(request, 'store/homepage.html')


def about(request):
    return render(request, 'store/about.html')
