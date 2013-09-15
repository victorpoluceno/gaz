from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^accounts/login/$', 'gaz.login.views.login', name='login'),
)
