# -*- coding: utf-8 -*-

u"""
Common document-related views.
"""

from django.shortcuts import get_object_or_404
from django.views.generic.list_detail import object_list

from briefcase.models import Document, DocumentType


def document_list(request, queryset, template_name, extension=None, **kwargs):
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
    extra_context = kwargs.pop('extra_context', {})
    if extension is not None:
        # we could get around without this query for DocumentType,
        # but we want the type object to be accessible in the template
        document_type = get_object_or_404(DocumentType, extension__exact=extension.lower())
        extra_context['document_type'] = document_type
        queryset = queryset.filter(type=document_type)
    if 'template_object_name' not in kwargs:
        kwargs['template_object_name'] = 'document'
    return object_list(request, queryset, template_name=template_name, extra_context=extra_context, **kwargs)
