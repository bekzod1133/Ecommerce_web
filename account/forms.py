from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your views here.
class CreateUserF(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']