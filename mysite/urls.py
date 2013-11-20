from django.conf.urls import *
from mysite import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
# admin.autodiscover()
#from django.contrib import admin
#admin.autodiscover()
urlpatterns = patterns('mysite.views',
('^hello/$','hello'),('^time/$','current_datetime'),(r'^time/plus/(\d{1,2})/$','hours_ahead')
,('^dog/$','dog'),('^go/$','go'),('^display/$','display_meta'),
('^dis/$','display'),(r'^search/$','search'),(r'^contact/$','contact'),
(r'^contact/thanks/$','success'), ,(r'^admin/', include(admin.site.urls)),)
# Examples:    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
