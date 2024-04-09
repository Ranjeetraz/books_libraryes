from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.models import CustomUser
from app.models import CustomUser,Book
from app.models import BookTransaction1
from app.models import Book_return
from app.models import course_details
# from app.models import course_fee


class StudentRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username','role','course','pending_fee','email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(StudentRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['role'].choices = self.fields['role'].choices[2:]




class AdminRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username','role','email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(AdminRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['role'].choices = self.fields['role'].choices[:2:]
    
    




class UserLoginForm(AuthenticationForm):
    username=forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form.control'}))
    password=forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={'class':'form.control'}))






class bookform(forms.ModelForm):
    class Meta:
        model=Book
        fields= '__all__'  



class transaction_forms(forms.ModelForm):
    class Meta:
        model= BookTransaction1  
        fields= '__all__'


class Book_return_form(forms.ModelForm):
    class Meta:
        model= Book_return
        fields= '__all__'



class course_details_form(forms.ModelForm):
    class Meta:
        model= course_details
        fields= '__all__'      


# class course_fee_from(forms.ModelForm):
#     class Meta:
#         model= course_fee
#         fields= '__all__'      
