############################
## ACCOUNTS VIEWS.PY FILE ##
############################

from django.views.generic import CreateView
from accounts.forms import UserCreateForm
from django.urls import reverse_lazy
from django.contrib.auth import login

class SignUp(CreateView):

	template_name = 'accounts/signup.html'
	form_class = UserCreateForm
	success_url = reverse_lazy('login')