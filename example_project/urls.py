from django.conf import settings
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^example_project/', include('example_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('briefcase.views',
    url(r'^$',                                  'general.recent_documents', name='recent_documents'),
    url(r'^my_documents/$',                     'per_user.my_documents',    name='my_documents'),
    url(r'^my_documents/(?P<extension>\w+)/$',  'per_user.my_documents',    name='my_documents_by_extension'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', 
         {'document_root': settings.MEDIA_ROOT}),
    )
