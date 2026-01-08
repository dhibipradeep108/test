from django.urls import path
from . import views
from django.views.generic.dates import ArchiveIndexView
from .models import Article

urlpatterns = [
    path('article/today/', views.ArticleTodayArchive.as_view(), name = "article_today_archive"),
    path('article/<int:year>/week/<int:week>/', views.ArticleWeekArchive.as_view(), name = "article_week_archive"),
    path('article/<int:year>/<int:month>/', views.ArticleMonthArchive.as_view(month_format = "%m"), name = "article_month_archive_numeric"),
    path('article/<int:year>/<str:month>/', views.ArticleMonthArchive.as_view(), name = "article_month_archive"),
    path('article/<int:year>/', views.ArtileYearArchive.as_view(), name = "article_year_archive"),
    path('archive/', ArchiveIndexView.as_view(model = Article, date_field = "pub_date", allow_future = True), name = "article_archive"),
    path('article/<int:year>/<str:month>/<int:day>/', views.ArticleDayArchive.as_view(), name = "article_day_archive"),
    path('author_list/', views.author_list , name = 'author_list'),
    path('author_detail/<int:pk>/', views.author_detail, name = "author_detail"),
    path('article_detail/<int:pk>/', views.article_detail, name = "article_detail"),
    path('create_author/', views.AuthorCreateView.as_view(), name = 'create_author'),
    path('update_author/<int:pk>/', views.AuthorUpdateView.as_view(), name = 'update_author'),
    path('delete_author/<int:pk>/', views.AuthorDeleteView.as_view(), name = 'delete_author'),
]