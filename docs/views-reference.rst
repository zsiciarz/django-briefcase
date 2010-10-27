================================
Document-related views reference
================================

This is a detailed reference of view functions provided by ``django-briefcase``.


``briefcase.views.document_list``
---------------------------------

A very thin wrapper for the generic ``object_list`` view.
    
Currently we supply here only the ``template_object_name`` argument, but
more functionality may come and it is good to keep the generic document
list in one place.
This also allows for a greater customization by setting some view arguments
in the URLconf.

Template receives a ``document_list`` context variable which is a QuerySet
instance.


``briefcase.views.general.recent_documents``
--------------------------------------------

Renders a list of all documents sorted by creation date.


``briefcase.views.general.download_document``
---------------------------------------------

Sends the document to the browser.


``briefcase.views.per_user.my_documents``
-----------------------------------------

Renders a list of all documents added by current user.


``briefcase.views.per_user.documents_for_user``
-----------------------------------------------

Renders a list of documents added by a specific user.

The user can be identified by his username or user_id. If both are 
specified, username takes precedence.
