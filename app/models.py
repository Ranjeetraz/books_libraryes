from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User



class course_details(models.Model):
    course=models.CharField(max_length=20)
    duration=models.CharField(max_length=40)
    Total_fee=models.IntegerField()

    def __str__(self):
        return self.course

class CustomUser(AbstractUser):
    ROLES = [
            ("0",'admin'),
            ("1", 'student'),
        ]

    role = models.CharField(choices=ROLES,max_length=200)
    course= models.ForeignKey(course_details,  null=True , blank=True ,on_delete=models.CASCADE, related_name='studentname')
    pending_fee=models.BooleanField(default=False)
    



class payment(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='Custname')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_paid = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.student.username







class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=50)
    published_date = models.DateField()
    bookquantity_no=models.IntegerField(default=3)

    def __str__(self):
        return self.title





class BookTransaction1(models.Model):
    student= models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='Custnamne')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='Books')
    transaction_date = models.DateField()
    return_date = models.DateField()




    def __int__(self):
        return self.transaction_date


    

      

class Book_return(models.Model):
    student= models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='studentname')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='bookname')
    return_date = models.DateField()
    late_return_date= models.DateField(blank=True,null=True)
    late_charge_rate=models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.student.username

    








    
# class course_fee(models.Model):
#     student= models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='student1_name')
#     course= models.ForeignKey(course_details, on_delete=models.CASCADE, related_name='studentname')
#     pending_fee=models.BooleanField(default=True)


#     def __str__(self):
#         return self.student.username


    

   