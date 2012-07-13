from django.conf.urls import patterns, include, url
from health_direct.views import home, testsearch, testgenerate 

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',	
	('^home/$', home),
	('^search/$', testsearch),
	('^testbuilder/$', testgenerate),	
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
