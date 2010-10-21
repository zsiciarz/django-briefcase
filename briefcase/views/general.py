# -*- coding: utf-8 -*-

u"""
General document-related views (recent docs, top downloads etc).
"""

from briefcase.views import document_list
from briefcase.models import Document


def recent_documents(request, **kwargs):
    u"""
    Renders a list of all documents sorted by creation date.
    """
    queryset = Document.objects.all().order_by('-added_at')
    return document_list(request, queryset, "briefcase/recent_documents.html", **kwargs)
