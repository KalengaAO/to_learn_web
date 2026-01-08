from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question

def index(resquest):
  list_ = Question.objects.order_by("-pub_date")[:5]
  return render(resquest, "polls/index.html", {"lista": list_})

def detail(resquest, id):
    try:
        questao = Question.objects.get(pk=id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist!")
    return render(resquest, "polls/detail.html", {"resposta": questao})

def results(request, id):
    response = "You are looking at the result of question %s"
    return HttpResponse(response % id)

def vote(request, id):
    response = "You are looking at the result of question %s"
    return HttpResponse(response % id)