from django import forms
from django.contrib.auth.forms import UserCreationForm

from Loan.models import Advisor

class CreateUserForm(UserCreationForm):
    
    class Meta():
        model = Advisor
        include = ('username', 
                    'email', 'first_name','password')
        exclude = ('deleted','contact_no','pancard_info','city','state','postalCode','address', 'referred_by', 'groups', 'password', 'profile_pic',
                    'user_permissions','is_verified', 'date_joined', 'last_login', 'is_superuser','is_staff','is_active')

