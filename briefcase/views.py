# -*- coding: utf-8 -*-

u"""
Document-related views.
"""

from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _
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

def recent_documents(request, **kwargs):
    u"""
    Renders a list of all documents sorted by creation date.
    """
    queryset = Document.objects.all().order_by('-added_at')
    return document_list(request, queryset, "briefcase/recent_documents.html", **kwargs)

@login_required
def my_documents(request, **kwargs):
    u"""
    Renders a list of all documents added by current user.
    
    We need a User here, not an AnonymousUser, so the view is wrapped with
    login_required decorator.
    """
    queryset = Document.objects.filter(added_by=request.user)
    return document_list(request, queryset, "briefcase/my_documents.html", **kwargs)

def documents_for_user(request, username=None, user_id=None, **kwargs):
    u"""
    Renders a list of documents added by a specific user.
    
    The user can be identified by his username or user_id. If both are 
    specified, username takes precedence.
    """
    if username is not None:
        queryset = Document.objects.filter(added_by__username=username)
    elif user_id is not None:
        queryset = Document.objects.filter(added_by_id=user_id)
    else:
        raise AttributeError(_("documents_for_user requires either username or user_id."))
    return document_list(request, queryset, "briefcase/documents_for_user.html", **kwargs)
