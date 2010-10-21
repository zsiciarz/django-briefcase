# -*- coding: utf-8 -*-

u"""
Templatetags definitions.
"""

from django.template import Library, Node, TemplateSyntaxError
from django.utils.translation import ugettext_lazy as _

from briefcase.models import DocumentType


register = Library()


def do_get_document_types(parser, token):
    u"""
    Retrieves a list of all distinct document types found in the database.
    """
    # for a call like this: {% get_document_types as document_types %}
    # bits elements are: 0 - tag name, 1 - 'as', 2 - variable name
    bits = token.split_contents()
    if len(bits) != 3:
        raise TemplateSyntaxError(_("%s requires 2 arguments") % bits[0])
    if bits[1] != 'as':
        raise TemplateSyntaxError(_("Second argument of %s must be 'as'") % bits[0])
    as_varname = bits[2]
    return DocumentTypesNode(as_varname)


class DocumentTypesNode(Node):
    u"""
    Inserts document type list into the template context.
    """
    def __init__(self, as_varname):
        self.as_varname = as_varname
    
    def render(self, context):
        document_types = DocumentType.objects.exclude(extension__exact='').order_by('extension')
        context[self.as_varname] = document_types
        return ''


register.tag('get_document_types', do_get_document_types)
