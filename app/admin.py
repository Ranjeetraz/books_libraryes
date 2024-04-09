from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app.models import CustomUser
from app.models import Book
from app.models import BookTransaction1
from app.models import Book_return
from app.models import course_details
from app.models import payment
# from app.models import course_fee

   
admin.site.register(CustomUser)
admin.site.register(Book)
admin.site.register(BookTransaction1)
admin.site.register(Book_return)
admin.site.register(course_details)
admin.site.register(payment)
# admin.site.register(course_fee)




# class CustomUserAdmin(UserAdmin):
#     list_display = ('username', 'email', 'is_student', 'is_admin')
#     list_filter = ('is_student', 'is_admin')
#     fieldsets = (
#         (None, {'fields': ('username', 'email', 'password')}),
#         ('Permissions', {'fields': ('is_student', 'is_admin', 'is_active')}),
#     )

# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('user', 'roll_number')

# class BookAdmin(admin.ModelAdmin):
#     list_display = ('name', 'author')