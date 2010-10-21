# -*- coding: utf-8 -*-

u"""
General document-related views (recent docs, top downloads etc).
"""

from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from briefcase.views import document_list
from briefcase.models import Document


def recent_documents(request, **kwargs):
    u"""
    Renders a list of all documents sorted by creation date.
    """
    queryset = Document.objects.all().order_by('-added_at')
    return document_list(request, queryset, "briefcase/recent_documents.html", **kwargs)


def download_document(request, document_id):
    u"""
    Sends the document to the browser.
    
    Needs some kind of access control. Is the current user authorized to look at
    these (possibly classified...?) data? For now, just allow everybody. Or,
    maybe, set up an access policy somewhere else and check it here.
    """
    document = get_object_or_404(Document, pk=document_id)
    response = HttpResponse(content=document.file, mimetype=document.type.mimetype)
    response['Content-Disposition'] = 'attachment; filename=%s' % document.get_filename()
    return response
