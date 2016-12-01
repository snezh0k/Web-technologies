from django.shortcuts import render, get_object_or_404
from django.middleware import csrf
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage
from .models import Question, Answer
from .forms import AskForm, AnswerForm
# Create your views here.

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def home(request):
    questions = Question.objects.new()
    page, paginator = paginate(request, questions)
    paginator.baseurl = '/?page='
    return render(request, 'question/main.html', 
                  {
                      'questions' : page.object_list,
                      'page' : page,
                      'paginator' : paginator,
                   })


def show_popular(request):
    questions = Question.objects.popular()
    page, paginator = paginate(request, questions)
    paginator.baseurl = '/popular/?page='

    return render(request, 'question/main.html',
                  {
                  'questions' : page.object_list,
                  'page' : page,
                  'paginator' : paginator,
                  })
        
def show_question(request, qn):
    question = get_object_or_404(Question, pk=qn)
    answers = Answer.objects.all().filter(question=question)
    
    if request.method == "POST":
        form = AnswerForm(request.POST, initial={'question':qn})
        if form.is_valid():
            answer = form.save()
            url = '/question/' + qn + '/'
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm(initial={'question':qn})
        return render(request, 'question/one.html',
                  {
                      'question' : question,
                      'answers' : answers,
                      'form' : form,
                      'qn' : qn,
                   })

def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except (EmptyPage, ValueError):
        raise Http404
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page, paginator

def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    elif request.method == "GET":
         form = AskForm()
         return render(request, 'question/ask.html',
                  {
                      'form' : form,
                  })
