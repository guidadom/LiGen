from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.main_page, name='Benvenuto'),
	url(r'^login', views.login, name='Login'),
]

