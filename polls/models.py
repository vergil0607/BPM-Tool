import datetime

from django.db import models
from django.utils import timezone
import django_tables2 as tables


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date Published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class ExternalData(models.Model):
    Mitarbeiter_ID = models.CharField(max_length=200)
    Leistungsdatum = models.CharField(max_length=200)
    Taetigkeit = models.CharField(max_length=200)
    Kostenstelle = models.CharField(max_length=200)
    Bundesland = models.CharField(max_length=200)

    def __str__(self):
        return self.Mitarbeiter_ID


class Ausschreibungen(models.Model):
    Nummer = models.CharField(max_length=200)
    Name = models.CharField(max_length=200)
    Status = models.CharField(max_length=200)
    Auftraggeber = models.CharField(max_length=200)
    Region = models.CharField(max_length=200)
    Auftragswert = models.CharField(max_length=200)
    Beguenstigter = models.CharField(max_length=200)
    DatumNotifikation = models.CharField(max_length=200)

    def __str__(self):
        return self.Nummer


class DjangoTable(tables.Table):
    class Meta:
        model = ExternalData


