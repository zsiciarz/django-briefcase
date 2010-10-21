# -*- coding: utf-8 -*-

u"""
Common document-related views.
"""

from django.views.generic.list_detail import object_list

from briefcase.models import Document


def document_list(request, queryset, template_name, **kwargs):
    u"""
    A very thin wrapper for the generic ``object_list`` view.
    
    Currently we supply here only the ``template_object_name`` argument, but
    more functionality may come and it is good to keep the generic document
    list in one place.
    This also allows for a greater customization by setting some view arguments
    in the URLconf.
    
    Template receives a ``document_list`` context variable which is a QuerySet
    instance.
    """
    if 'template_object_name' not in kwargs:
        kwargs['template_object_name'] = 'document'
    return object_list(request, queryset, template_name=template_name, **kwargs)
