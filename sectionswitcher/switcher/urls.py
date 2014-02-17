from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from switcher import views

urlpatterns = patterns('',
	url(r'^$', views.home, name="home"),
)
