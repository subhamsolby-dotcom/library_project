from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm, MemberForm, BorrowForm


def home(request):
    return render(request, 'library/home.html')


def add_book(request):
    form = BookForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('book_list')

    return render(request, 'library/add_book.html', {'form': form})


def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})


def add_member(request):
    form = MemberForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'library/add_member.html', {'form': form})


def borrow_book(request):
    form = BorrowForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'library/borrow_book.html', {'form': form})

# Create your views here.
