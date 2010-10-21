# -*- coding: utf-8 -*-

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
