from Book.models import Book

#exec(open("D:\\VSCODE\\Python\\Django\\Library\\Book\\db_shell.py").read())
'''
all_data= Book.objects.all()
print(all_data)
print("-"*10)

sid = 2
b1 = Book.objects.get(id=sid)
print(b1)
print("-"*10)

b2 = Book.objects.create(name="MNOP",author="QRST",qty= 34, price= 234)
print(b2.id)
print("-"*10)

sid= 5
b3 = Book.objects.get(id=sid)
b3.name = "Mohini"
b3.save()
print("-"*10)

sid = 7
b4 = Book.objects.get(id=sid)
b4.delete()
'''

# all_data= Book.objects.all()
# print(all_data)
'''
for book in all_data:
    print("--------BOOK FOR ID NUMBER", book.id, "----------")
    print("Book Name: ",book.name)
    print("Book Author: ",book.author)
    print("Book Quantity: ",book.qty)
    print("Book Price: ",book.price)
'''

'''
for book in all_data:
    book.qty= 15
    book.save()

'''
'''

for book in all_data:
    print(book.__dict__)

'''
'''
all_data = Book.objects.all().values("id","name","price")
for book in all_data:
    print(book)

all_data = Book.objects.all().values_list()
print(all_data)

'''
'''
import random

for i in range(1,26):
    # TypeError: an integer is required (got type list)
    # b = Book(name= chr(random.sample(range(65,90),4)), author="ABC", qty= (random.sample(range(23,67),2)), price=(random.sample(range(200,600),4)))
    b = Book(name= chr(random.randint(65,90))*4, author="ABC", qty= random.randint(13,34), price= random.randint(200,400))
    b.save()
'''
'''
b1= Book.objects.filter(id__gt=15)
print(b1)
for i in b1:
    print(i.__dict__)

'''

# b1= Book.objects.filter(name__istartswith='v').values("id","name")
# for i in b1:
#     print(i)

# b3 = Book.objects.all().order_by("-name")
# print(b3)

# b4 = Book.objects.all().count()
# print(b4)

# l = [i for i in range(12,20)]
# books = Book.objects.all().exclude(id__in=l)
# print(books)