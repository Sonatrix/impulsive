from django import forms
from django.contrib.auth.forms import UserCreationForm

from Loan.models import Advisor

class CreateUserForm(UserCreationForm):
    
    class Meta():
        model = Advisor
        include = ('username', 
                    'email', 'first_name','password')
        exclude = ('deleted', 'referred_by', 'groups', 'password', 'profile_pic',
                    'user_permissions', 'date_joined', 'last_login','is_superuser','is_staff','is_active')

