from django.conf.urls import patterns, include, url
from health_direct.views import home, inputsearch, questionbuilder, questionbuilt, build, success
from health_direct.CheckupIterator.views import CheckupIterator
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
ci = CheckupIterator()

urlpatterns = patterns('',
	('^accounts/login/$', login),
	('^accounts/logout/$', logout),
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
