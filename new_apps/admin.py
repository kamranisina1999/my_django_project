from django.contrib import admin

from books.models import Book, Author


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'isbn_code', 'publish_date', 'author_name']
    list_filter = ['author']
    search_fields = ['title', 'author__last_name', 'author__first_name']

    def author_name(self, obj):
        return f'{obj.author.first_name} {obj.author.last_name}'


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
