from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from switcher import views

urlpatterns = patterns('',
	url(r'^thanks/$', views.thanks, name="thanks"),
	url(r'^getCourses$', views.getCourses, name="getCourses"),
	url(r'^getSections$', views.getSections, name="getSections"),
	url(r'^verify/([0-9a-f]{32})$', views.verify, name="verify"),
    url(r'^confirm/([0-9a-f]{32})$', views.confirm, name="confirm"),
	url(r'^.*$', views.home, name="home"),
)
