from django.shortcuts import render
from .models import Author, Book
# Create your views here.
def home (request):
    author = Author.objects.all()
    book = Book.objects.all()
    return render(request,'home.html',{'author':author, 'book':book})

def welcome (request,name=None):
    if name is None:
        name= request.GET.get('name','guest')
    context = {'user_name':name}
    return render(request,'welcome.html',context)