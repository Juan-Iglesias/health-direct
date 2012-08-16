from django.conf.urls import patterns, include, url
from health_direct.views import home, inputsearch, questionbuilder, questionbuilt, testtags
from health_direct.CheckupIterator.views import CheckupIterator

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
ci = CheckupIterator()

urlpatterns = patterns('',	
	('^home/$', home),
	('^testtags/$', CheckupIterator.as_view()),
	('^search/$', inputsearch),
	('^questionbuilder/$', questionbuilder),
	('^questionbuilder/successful$', questionbuilt),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
