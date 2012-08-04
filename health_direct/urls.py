from django.conf.urls import patterns, include, url
from health_direct.views import home, inputsearch, questionbuilder, questionbuilt, testtags

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',	
	('^home/$', home),
	('^testtags/$', testtags),
	('^search/$', inputsearch),
	('^questionbuilder/$', questionbuilder),
	('^questionbuilder/successful$', questionbuilt),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
