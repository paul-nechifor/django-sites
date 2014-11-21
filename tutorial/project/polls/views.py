from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Polls index.')

def detail(request, question_id):
    return HttpResponse('Question %s.' % question_id)

def results(request, question_id):
    return HttpResponse('Results for question: %s.' % question_id)

def vote(request, question_id):
    return HttpResponse('Vote on question: %s.' % question_id)
