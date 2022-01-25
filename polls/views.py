from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView
from .models import Question, Choice, ExternalData, Ausschreibungen


def base(request):
    return render(request, 'layouts/base.html')


def main(request):
    return render(request, 'main.html')


def home(request):
    return render(request, 'layouts/home.html')


def processes(request):
    return render(request, 'layouts/processes.html')


def data(request):
    edata = Ausschreibungen.objects.all()
    context = {
        'Ausschreibungen': edata
    }
    return render(request, 'layouts/data.html', context)


def newData(request):
    return render(request, 'layouts/newData.html')


def analytics(request):
    return render(request, 'layouts/analytics.html')


def dev(request):
    return render(request, 'layouts/dev.html')


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You did not select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# Create your views here.

