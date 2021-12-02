from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Question, Answer

# Test views
def test(request, *args, **kwargs):
    return HttpResponse('OK')

# Paginator for questions
def paginate_questions(request, qs):
    limit = 10
    page = request.GET.get('page', 1)
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page

# View for main page: show new questions(/, /new/)
def new_questions(request):
    question_list = Question.objects.new()
    questions = paginate_questions(request, question_list)
    return render(request, 'new.html', {
        "questions": questions,
    })

# View for page with popular questions(/popular/)
def popular_questions(request):
    question_list = Question.objects.popular()
    questions = paginate_questions(request, question_list)
    return render(request, 'popular.html', {
        "questions": questions,
    })

# View for work with specific question
def question_details(request, id = None):
    question = get_object_or_404(Question, id = id)
    answers = question.answer_set.all()
    return render(request, 'question.html', {
        'question': question,
        'answers': answers,
    })
