from django.urls import path
from django.conf import settings
from demo.views import DemoView

app_name = 'demo'

urlpatterns = [
    path('', DemoView.as_view(template_name = 'pages/demo/index.html'), name='index'),

    path('error', DemoView.as_view(template_name = 'non-exist-file.html'), name='Error Page'),
]