from django.contrib import admin, messages
from .models import Article, Author, Person, Blog, Group
from django.utils.translation import ngettext

@admin.action(description = "Mass Withdraw")
def make_withdrawn(modeladmin, request, queryset) :
    queryset.update(status = 'w')

class ArticleAdmin(admin.ModelAdmin) :
    fields = [('title', 'status'), 'author','pub_date']
    list_display = ['__str__', 'author__name','status', 'pub_date']
    ordering = ['title']
    @admin.action(description = "Mass publishing")
    def make_published(self, request, queryset) :
        updated = queryset.update(status = 'p')
        self.message_user(
            request,
            ngettext(
                "%d story was published",
                "%d stories was published",
                updated,
            ) % updated,
            messages.SUCCESS,
        )
    actions = [make_published, make_withdrawn]
 
class BlogInline(admin.TabularInline) :
    model = Blog 

class MembershipInline(admin.TabularInline) :
    model = Group.members.through

class PersonAdmin(admin.ModelAdmin) :
    inlines = [BlogInline]
    list_display = ['__str__','f_name', 'l_name', 'colored_name']

class GroupAdmin(admin.ModelAdmin) :
    inlines = [MembershipInline]

class BlogAdmin(admin.ModelAdmin) :
    list_display = ["title", 'author', 'f_name']
    prepopulated_fields = {'slug' : ["title"]}
    # show_facets = admin.ShowFacets.ALWAYS
    @admin.display(ordering = "author__f_name")
    def f_name(self, obj) :
        return obj.author.f_name

admin.site.register(Article, ArticleAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Blog, BlogAdmin)