from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [

    url(r'^signup/$', views.SignupView, name="signup"),
    url(r'^login/$', views.LoginView, name="login"),
    url(r'^logout/$', views.LogoutView, name="logout"),


]
