# -*- coding: utf-8 -*-

from django.test import TestCase
from briefcase.models import DocumentType

class DocumentTypeTest(TestCase):
    def setUp(self):
        import mimetypes
        self.mimetypes = (('doc' + extension, mimetype) 
                          for extension, mimetype in mimetypes.types_map.iteritems())

    def test_unknown_type(self):
        document_type = DocumentType.unknown_type()
        self.assertEqual(document_type.mimetype, "application/octet-stream")
        self.assertEqual(document_type.name, "Unknown type")

    def test_type_for_file_string(self):
        for filename, mimetype in self.mimetypes:
            document_type = DocumentType.type_for_file(filename)
            self.assertEqual(document_type.mimetype, mimetype)
            self.assertEqual(document_type.name, mimetype)
