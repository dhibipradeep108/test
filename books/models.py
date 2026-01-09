from django.db import models
from django.urls import reverse
from django.contrib import admin
from django.utils.html import format_html

class Author(models.Model) :
    name = models.CharField(max_length = 100)
    def get_absolute_url(self):
        return reverse("author_detail", kwargs={"pk": self.pk})
    def __str__(self):
        return self.name

STATUS_CHOICES = {
    'p' : "Published",
    'd' : "Draft",
    "w" : "Withdrawn"
}

class Article(models.Model) :
    title = models.CharField(max_length = 200)
    pub_date = models.DateField("Publication Date")
    status = models.CharField(max_length = 1, choices = STATUS_CHOICES)
    author = models.ForeignKey(Author, on_delete = models.CASCADE, null = True)
    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})
    def __str__(self):
        return self.title

class Person(models.Model) :
    f_name = models.CharField("First Name", max_length = 75)
    l_name = models.CharField("Last Name", max_length = 75)
    color_code = models.CharField(max_length = 6)
    @admin.display()
    def colored_name(self) :
        return format_html(
            '<span style = "color: #{};">{} {}</span>',
            self.color_code,
            self.f_name,
            self.l_name,
        )
    def __str__(self):
        return f'{self.f_name} {self.l_name}'
    
class Group(models.Model) :
    name = models.CharField("Group Nsme", max_length = 50)
    members = models.ManyToManyField(Person, related_name = "groups")
    def __str__(self):
        return self.name
    
class Blog(models.Model) :
    title = models.CharField(max_length = 255)
    author = models.ForeignKey(Person, on_delete = models.CASCADE)
    slug = models.SlugField()
    def __str__(self):
        return self.title