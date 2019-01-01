from django.contrib import admin

from .models import BlogArticles

# Register your models here.

class BlogArticlesAdmin(admin.ModelAdmin):
    list_display = ("title","author","published")
    list_filter = ("published","author")
    search_fields = ('title',"body")
    raw_id_fields = ("author",)
    date_hierarchy = "published"
    ordering = ['published','author']

admin.site.register(BlogArticles,BlogArticlesAdmin)
