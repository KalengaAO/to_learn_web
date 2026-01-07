from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

def index(resquest):
    list_ = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.questão for q in list_])
    return HttpResponse(output)


def detail(request, id):
    response = "You are looking at question! %s"
    return HttpResponse(response % id)

def results(request, id):
    response = "You are looking at the result of question %s"
    return HttpResponse(response % id)

def vote(request, id):
    response = "You are looking at the result of question %s"
    return HttpResponse(response % id)