from django.contrib import admin

from .models import Author, Quote


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'birth_date', 'location']
    search_fields = ['name']
    list_filter = ['name']


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['text', 'author']
    search_fields = ['text', 'author__name']
    list_filter = ['author']
