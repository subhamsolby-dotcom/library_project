from django.contrib import admin
from .models import Book, Member, Borrow


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'quantity')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('author',)


class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')


class BorrowAdmin(admin.ModelAdmin):
    list_display = ('member', 'book', 'borrow_date', 'return_date')
    list_filter = ('borrow_date', 'return_date')
    search_fields = ('member__name', 'book__title')


admin.site.register(Book, BookAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Borrow, BorrowAdmin)

# Admin panel customization
admin.site.site_header = "Library Management Admin"
admin.site.site_title = "Library Admin Portal"
admin.site.index_title = "Welcome to Library Dashboard"