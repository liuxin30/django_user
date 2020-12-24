from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice, QuestionForm
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.get('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoexNotExist):
        return render(request, 'polls/detail.html', {'question':question,
                                                     'error_message':"You didn't select a choice.",})
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def add(request):
    HttpResponse("hello world")
    # q = Question().
    # question = QuestionForm(request.POST, instance=q)
    # if question.is_valid():
    #     question.save(commit=True)
    # return render(request, 'polls/index.html', {'latest_question_list':Question.objects.order_by('-pub_date')[:5]})


