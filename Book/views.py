from django.shortcuts import render, redirect
from django.http import HttpResponse
from Book.models import Book

def homepage(request):
    # all_books = Book.objects.all().filter(is_deleted='N')
    all_books = Book.active_objects.all()
    return render(request,template_name="welcome.html", context= {"books": all_books})

def save_book(request):
    # print(request.POST)
    b_name = request.POST.get("name")
    b_author = request.POST.get("auth")
    b_qty = request.POST.get("qty")
    b_price = request.POST.get("price")
    b_pub = request.POST.get("pub")
    if b_pub == "on":
        flag = True
    else:
        flag = False
    if request.POST.get("id"):

        book_obj = Book.objects.get(id=request.POST.get("id"))
        book_obj.name = b_name
        book_obj.author = b_author
        book_obj.qty = b_qty
        book_obj.price = b_price
        book_obj.is_published = flag
        book_obj.save()
        return redirect('welcome')

    else:  
        b =Book(name=b_name, author=b_author, qty=b_qty, price=b_price, is_published=flag)
        b.save()
        return redirect('welcome')

def edit_book(request, id):
    try:
        book_obj = Book.objects.get(id=id)
    except Book.DoesNotExist:
        msg= f"The Entered Id is not Available in Database, You Entered:  {id}"
        return HttpResponse(msg)
    book_obj= Book.objects.get(id=id)
    # all_books = Book.objects.all().filter(is_deleted='N')
    all_books = Book.active_objects.all()
    return render(request,template_name="welcome.html", context= {"book": book_obj,"books": all_books})
    
def delete_book(request, pk):
    book_obj= Book.objects.get(id=pk)
    book_obj.is_deleted = 'Y'
    book_obj.save()
    # book_obj.delete()
    return redirect('welcome')

def delete_all(request):
    book_obj = Book.objects.all()
    for i in range(len(book_obj)):
        book_obj[i].is_deleted = 'Y'
        book_obj[i].save()
    return redirect('welcome')

def restore_all(request):
    book_obj = Book.objects.all()
    # book_obj.is_deleted = 'N'
    for i in range(len(book_obj)):
        book_obj[i].is_deleted = 'N'
        book_obj[i].save()
    return redirect('welcome')

def hard_delete_book(request, pk):
    book_obj= Book.objects.get(id=pk)
    book_obj.delete()
    return redirect('welcome')

def restore(request, pk):
    book_obj= Book.objects.get(id=pk)
    book_obj.is_deleted = 'N'
    book_obj.save()
    # book_obj.delete()
    return redirect('welcome')

def show_deleted_data(request):
    all_deleted_books = Book.inactive_objects.all()
    return render(request,template_name="welcome.html", context= {"books": all_deleted_books})

