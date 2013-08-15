from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^', 'gaz.home.views.index', name='home'),
)
