=====
Usage
=====

Right after :doc:`install` you can manage your documents from the Django admin 
site. To actually present them in the front-end, hook the application views 
into your URLconf.

Example::

    urlpatterns = patterns('briefcase.views',
        #...
        url(r'^recent_documents/', 
            'general.recent_documents',
            name='recent_documents'
        ),
        url(r'^my_documents/', 
            'per_user.my_documents',
            name='my_documents'
        ),
        url(r'^download/(?P<document_id>\d+)/$',
            'general.download_document',
            name='download_document'
        ),
        #...
    )

Follow the :doc:`views-reference` for a detailed documentation of all views.
