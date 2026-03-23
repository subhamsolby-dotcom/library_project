from django import forms
from .models import Book, Member, Borrow


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'


class BorrowForm(forms.ModelForm):
    class Meta:
        model = Borrow
        fields = '__all__'