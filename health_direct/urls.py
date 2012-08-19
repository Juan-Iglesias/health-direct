from django.conf.urls import patterns, include, url
from health_direct.views import home, inputsearch, questionbuilder, questionbuilt, build, success, my_login
from health_direct.CheckupIterator.views import CheckupIterator

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
ci = CheckupIterator()

urlpatterns = patterns('',
	('^login/$', my_login),	
	('^home/$', ci.get_checkup),
	('^search/$', inputsearch),
	('^questionbuilder/$', questionbuilder),
	('^questionbuilder/successful$', questionbuilt),
	('^posttest/$', build),
	('^posttest/successful/$', success),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
