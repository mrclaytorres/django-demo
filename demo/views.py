from django.views.generic import TemplateView
from django.http import HttpResponse
from django.conf import settings
from django.urls import resolve
from _keenthemes.__init__ import KTLayout
from _keenthemes.libs.theme import KTTheme
from pprint import pprint
from .models import Product

class DemoView(TemplateView):
	template_name = 'pages/demo/index.html'

	def get_context_data(self, **kwargs):

		all_products = Product.objects.all

		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)

		# A function to init the global layout. It is defined in _keenthemes/__init__.py file
		context = KTLayout.init({'all': all_products})

		return context