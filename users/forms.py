from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from library.models import Profile
# from django.contrib.auth.forms import 

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2' )


Branch_choices = (
    ('1','Electronics'),
    ('2','Computer Science'),
    ('3','Information Technology'),
    ('4','Production'),
    ('5','Civil'),
    ('6','Mechanical'),
    ('7','Electrical'),
    ('8','Chemical'),
    ('9','Instrumentation'),
    ('10','Textile')
)

Year_choices = (
    ('1','FirstYear BTECH'),
    ('2','SecondYear BTECH'),
    ('3','ThirdYear BTECH'),
    ('4','FourthYear BTECH'),
    ('5','FiveYear BTECH'),
    ('6','SixYear BTECH'),
)
        
class ProfileCReationForm(forms.Form):

    reg_no = forms.CharField(widget = forms.TextInput(attrs={'class':'inputs'}))
    Branch =  forms.ChoiceField(choices=Branch_choices) 
    Year = forms.ChoiceField(choices=Year_choices)  
    class Meta:
        model = Profile 
        fields = ('reg_no','Branch','Year')
