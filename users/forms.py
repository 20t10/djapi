from django_registration.forms import RegistrationForm
from django.contrib.auth import get_user_model


from users.models import CustomUser
User = get_user_model()
class CustomUserForm(RegistrationForm):

    class Meta(RegistrationForm.Meta):
        model = CustomUser
