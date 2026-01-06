from django.shortcuts import render
from .models import Article

def archive(request, year):
    a_list = Article.objects.filter(pub_date__year)
    context = {"year": year, "article_list": a_list}

    return render(request, "article/archive.html", context)