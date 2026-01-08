from django.db import models
from django.urls import reverse

class Author(models.Model) :
    name = models.CharField(max_length = 100)
    def get_absolute_url(self):
        return reverse("author_detail", kwargs={"pk": self.pk})
    def __str__(self):
        return self.name
    
class Article(models.Model) :
    title = models.CharField(max_length = 200)
    pub_date = models.DateField()
    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})
    def __str__(self):
        return self.title    