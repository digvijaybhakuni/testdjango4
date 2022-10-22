from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Question
from django.http import HttpResponse


def index(request):
    question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in question_list])
    return HttpResponse(output)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404(f'Question not found : {question_id}')
    return HttpResponse(f'You\'re looking at question text : {question.question_text}')


def results(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    output = '<br/>'.join([f'{c.choice_text} -- {c.votes}' for c in q.choice_set.all()])
    return HttpResponse(output)


def vote(request, question_id):
    return HttpResponse(f'You\'re looking at question vote: {question_id}')
