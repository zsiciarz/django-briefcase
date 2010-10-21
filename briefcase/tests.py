# -*- coding: utf-8 -*-

from django import template
from django.test import TestCase
from briefcase.models import DocumentType

class DocumentTypeTestCase(TestCase):
    def setUp(self):
        import mimetypes
        self.mimetypes = mimetypes.types_map.iteritems()

    def test_unknown_type(self):
        document_type = DocumentType.unknown_type()
        self.assertEqual(document_type.mimetype, "application/octet-stream")
        self.assertEqual(document_type.name, "Unknown type")

    def test_type_for_file_string(self):
        for extension, mimetype in self.mimetypes:
            filename = 'doc' + extension
            document_type = DocumentType.type_for_file(filename)
            self.assertEqual(document_type.mimetype, mimetype)
            
    def test_name_from_extension(self):
        for extension, mimetype in self.mimetypes:
            filename = 'doc' + extension
            document_type = DocumentType.type_for_file(filename)
            # for example: 'DOC Document'
            expected_name = extension[1:].upper() + ' Document'
            self.assertEqual(document_type.name, expected_name)

    def test_type_for_file_returns_the_same_type_object_after_editing(self):
        u"""
        We have to avoid creating multiple DocumentType objects for the same extension.
        
        This test checks that after some kind of a modification to one type object,
        another one will not be created when calling type_for_file with the same file type.
        """
        # retrieve a DocumentType for some arbitrary file
        document_type = DocumentType.type_for_file("test.txt")
        first_id = document_type.id
        # now let's change the name just like the administrator would do
        document_type.name = u'Text file'
        document_type.save()
        # and now find the type for another file
        another_type = DocumentType.type_for_file("another.txt")
        second_id = another_type.id
        self.assertEqual(first_id, second_id)


class TemplateTagsTestCase(TestCase):
    u"""
    Utility class for testing template tags.
    """
    def setUp(self):
        u"""
        Initializes an empty template context - just in case.
        """
        self.context = template.Context({})
        
    def render(self, template_content):
        t = template.Template(template_content)
        return t.render(self.context)

    def assertIncorrectSyntax(self, template_content):
        def _render(template_content):
            t = template.Template(template_content)
            t.render(self.context)
        self.assertRaises(template.TemplateSyntaxError, _render, template_content)
    
    def assertContextHasntVariable(self, variable_name):
        self.assertFalse(variable_name in self.context)
            
    def assertContextHasVariable(self, variable_name):
        self.assertTrue(variable_name in self.context)


class DocumentTemplateTagsTestCase(TemplateTagsTestCase):
    u"""
    Tests for the {% get_document_types %} template tag.
    """
    def test_get_document_types_raises_without_arguments(self):
        template_content = u"""
        {% load document_tags %}
        {% get_document_types %}
        """
        self.assertIncorrectSyntax(template_content)

    def test_get_document_types_raises_with_bad_arguments(self):
        template_content = u"""
        {% load document_tags %}
        {% get_document_types for me %}
        """
        self.assertIncorrectSyntax(template_content)

    def test_get_document_types_creates_context_variable(self):
        template_content = u"""
        {% load document_tags %}
        {% get_document_types as document_types %}
        """
        # sanity check
        self.assertContextHasntVariable('document_types')
        self.render(template_content)
        self.assertContextHasVariable('document_types')
