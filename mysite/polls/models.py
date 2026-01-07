from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):
    questão = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Data da publicação")

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def __str__(self):
        return self.questão

class Choice(models.Model):
    questão = models.ForeignKey(Question, on_delete=models.CASCADE)
    escolha = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.escolha