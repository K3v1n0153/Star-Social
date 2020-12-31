##############################
## SM_PROJECT VIEWS.PY FILE ##
##############################

from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse

class LoginPage(TemplateView):

	template_name = 'loginpage.html'

class ThanksPage(TemplateView):

	template_name = 'thankspage.html'

class HomePage(TemplateView):

	template_name = 'homepage.html'

	def get(self, request, *args, **kwargs):

		if request.user.is_authenticated:
			return HttpResponseRedirect(reverse('loginpage'))
		return super().get(request, *args, **kwargs)