from django.shortcuts import render
from .models import Book, Autor

def index(request):
    list_book = Book.objects.all()
    return render(request, "gestao/index.html", {"book": list_book})