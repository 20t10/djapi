from django_registration.forms import RegistrationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from users.models import CustomUser
User = get_user_model()
class CustomUserForm(RegistrationForm):

    class Meta(RegistrationForm.Meta):
        model = CustomUser
