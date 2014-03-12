from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'myapp.views.home', name='home'),
)
