from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


from app.forms import  StudentRegistrationForm,bookform
from app.forms import  transaction_forms
from app.forms import Book_return_form
from app.forms import course_details_form
from app.forms import AdminRegistrationForm
# from app.forms import course_fee_from





from .models import Book
from django.contrib import messages
from app.models import Book
from app.models import  BookTransaction1
from app.models import course_details
from app.models import Book_return
from app.models import CustomUser





def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # authenticate and login the user
            return redirect('/login')
            
    else:
        form = StudentRegistrationForm()
    return render(request, 'student_registation.html', {'form': form})





def student_register_history(request):
    # data=CustomUser.objects.filter(role=1)
    data=CustomUser.objects.filter(role='1')
    return render(request,'student_register_history.html',{'data1':data})







def admin_register(request):
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
            
    else:
        form = AdminRegistrationForm()
    return render(request, 'admin.register.html', {'form': form})



def admin_register_history(request):
    data=CustomUser.objects.filter(role='0')
    return render(request,'admin_register_history.html',{'data1':data})



        

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.role == '1':
                login(request, user)
                return redirect('/home')
            elif user.role == '0':
                login(request, user)
                return redirect('/admin')
            else:
                messages.error(request, 'Incorrect username or password.')
        else:
            messages.error(request, 'Incorrect username or password.')
            return redirect('/login')
    else:
        return render(request, 'student_login.html')




def add_book(request):

    if request.method == 'POST':
        form = bookform(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            book = Book.objects.filter(title=title).filter()
            if book: 
                book = Book.objects.get(title=title)
                bookquantity_no= form.cleaned_data.get('bookquantity_no')
                book.bookquantity_no += bookquantity_no
                book.save()
            else:
                form.save()      
    else:
        form = bookform()
    return render(request, 'add_book.html', {'form': form})




def book_list(request):
    all=Book.objects.all()
    return render(request,'admin_book_list.html',{'data':all})  




def home(request):
    return render(request,'home.html')
def admin(request):
    return render(request,'admin.html')



def take_book(request):
    if request.method == 'POST':
        form = transaction_forms(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('book')
            books = Book.objects.get(title=title)
            if books and books.bookquantity_no > 0: 
                books.bookquantity_no = books.bookquantity_no-1
                books.save()
                form.save()
            
                return redirect('/transa_book')  
            else:
                pass
        else:
            pass      
    else:
        form = transaction_forms()
    return render(request, 'book_transaction.html', {'form': form})




def transaction_book_list(request):
    all = BookTransaction1.objects.select_related('book','student').all()
    return render(request,'transaction_book_list.html',{'data':all})  



def return_book(request):
    if request.method == 'POST':
        form = Book_return_form(request.POST)
        if form.is_valid():

            title = form.cleaned_data.get('book')
            books = Book.objects.get(title=title)
            if books:
                books.bookquantity_no = books.bookquantity_no+1
                books.save()
                form.save()

                
                if form.cleaned_data.get('late_return_date'):
                    data = form.save(commit=False)
                    real_return_date = form.cleaned_data.get('return_date')
                    new_date = form.cleaned_data.get('late_return_date')
                    days=new_date - real_return_date
                    day = days.days
                    late_charge= form.cleaned_data.get('late_charge_rate')
                    fee=day*late_charge

                    a=int(fee)
                    data.late_charge_rate = a
                    form.save()

                return redirect('/booklist')
            else:
                pass
    
    form = Book_return_form()
    return render(request, 'return_book.html', {'form': form})


def return_book_list(request):
    all=Book_return.objects.all()
    return render(request,'return_book_list.html',{'data':all})  



def course_details_forms(request):
    if request.method == 'POST':
        form = course_details_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/course_details_history')
            
    else:
        form = course_details_form()
    return render(request, 'course_details_forms.html', {'form': form})




def course_details_history(request):
    data=course_details.objects.all()
    return render(request,'course_details_history.html',{'data1':data})
