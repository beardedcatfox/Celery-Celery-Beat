import cel
from cel.views import send_mail  # noqa: F401

from django.urls import path


urlpatterns = [
    path('send_mail/', cel.views.send_mail, name='send_mail'),
]
