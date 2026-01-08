from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.dates import YearArchiveView, MonthArchiveView, WeekArchiveView, DayArchiveView, TodayArchiveView
from .models import Author, Article
from django.urls import reverse_lazy

class AuthorCreateView(CreateView) :
    model = Author
    fields = ["name"]
    
class AuthorUpdateView(UpdateView) :
    model = Author
    fields = ['name']
    template_suffix = "_update_form"
    
class AuthorDeleteView(DeleteView) :
    model = Author
    success_url = reverse_lazy("author_list")

class ArtileYearArchive(YearArchiveView) :
    queryset = Article.objects.all()
    date_field = "pub_date"
    make_object_list = True
    allow_future = True
    
class ArticleMonthArchive(MonthArchiveView) :
    queryset = Article.objects.all()
    date_field = "pub_date"
    allow_future = True
    
class ArticleWeekArchive(WeekArchiveView) :
    queryset = Article.objects.all()
    date_field = "pub_date"
    week_format = '%W'
    allow_future = True
    
class ArticleDayArchive(DayArchiveView) :
    queryset = Article.objects.all()
    date_field = "pub_date"
    allow_future = True
    
class ArticleTodayArchive(TodayArchiveView) :
    queryset = Article.objects.all()
    date_field = "pub_date"
    allow_future = True

def author_detail(request, pk) :
    author = Author.objects.get(pk = pk)
    return render(request, 'books/authors.html', context = {"author" : author})

def article_detail(request, pk) :
    article = Article.objects.get(pk = pk)
    return render(request,'books/article.html', context = {"article" : article})

def author_list(request) :
    authors = Author.objects.all()
    return render(request, 'books/author_list.html', context = {"authors" : authors})