from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [

    url(r'^signup/$', views.SignupView, name="signup"),
]
