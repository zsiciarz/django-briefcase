# -*- coding: utf-8 -*-

import mimetypes
import os
from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.files import FieldFile
from django.utils.translation import ugettext_lazy as _


# additional mimetypes, for example Office 2007/2010 documents
mime_file = os.path.join(os.path.realpath(os.path.dirname(__file__)), 'data/mime.types')
type_map = mimetypes.read_mime_types(mime_file)
for extension, mime_type in type_map.iteritems():
    mimetypes.add_type(mime_type, extension)


class DocumentStatus(models.Model):
    u"""
    Status of the document.
    
    Defines document's stage in the workflow or just marks it as some custom
    status, eg. draft, unreviewed, published, etc.
    """
    name        = models.CharField(_("status name"), max_length=150, help_text=_("Displayed name of the document's status."))
    slug        = models.SlugField(max_length=150, unique=True, help_text=_("Slug name - important for the programmers."))
    description = models.CharField(_("status description"), max_length=250, blank=True, help_text=_("Status description - can be left empty."))
    
    class Meta:
        verbose_name = _("Document status")
        verbose_name_plural = _("Document statuses")
        ordering = ['-name']
        
    def __unicode__(self):
        return self.name


class DocumentType(models.Model):
    u"""
    File type (eg. PDF file, MS Word file etc.).
    """
    mimetype    = models.CharField(_("MIME type"), max_length=127, default="application/octet-stream", help_text=_("File MIME type as defined by <a href=\"http://tools.ietf.org/html/rfc4288#section-4.2\">RFC 4288</a>, for example: 'image/jpeg'"))
    name        = models.CharField(_("Full name"), max_length=250, blank=True, help_text=_("Human-readable name of the type, for example 'JPG Image'"))

    class Meta:
            verbose_name = _("Document type")
            verbose_name_plural = _("Document types")
            ordering = ['name']

    def __unicode__(self):
        if self.name:
            return self.name
        return self.mimetype

    @classmethod
    def unknown_type(cls):
        u"""
        Returns a default document type - a generic "Unknown type".
        
        This provides a sensible default value for a Document before saving it.
        """
        obj, created = cls.objects.get_or_create(mimetype="application/octet-stream",
                                                 name="Unknown type")
        return obj
    
    @classmethod
    def type_for_file(cls, file):
        if isinstance(file, FieldFile):
            filename = file.name
        else:
            filename = file
        mimetype, encoding = mimetypes.guess_type(filename)
        mimetype = mimetype or "application/octet-stream"
        obj, created = cls.objects.get_or_create(mimetype=mimetype, name=mimetype)
        return obj


class Document(models.Model):
    u"""
    The document itself.
    """
    # Basic document data.
    file = models.FileField(verbose_name=_("file"), upload_to='uploads/%Y/%m/%d/', help_text=_("This is the document itself - well, just a file."))
    type = models.ForeignKey(DocumentType, verbose_name=_("document type"), default=DocumentType.unknown_type, help_text=_("Document type, for example 'Microsoft Word Document' or 'PDF File'."))
    # Meta-information.
    status      = models.ForeignKey(DocumentStatus, verbose_name=_("document status"), null=True, blank=True)
    added_by    = models.ForeignKey(User, verbose_name=_("added by"), null=True, blank=True, editable=False)
    added_at    = models.DateTimeField(_("added at"), auto_now_add=True)
    updated_at  = models.DateTimeField(_("recently changed at"), auto_now=True)
    
    class Meta:
        verbose_name = _("Document")
        verbose_name_plural = _("Documents")
        ordering = ['-added_at']

    def __unicode__(self):
        return os.path.basename(self.file.name)

    def save(self, *args, **kwargs):
        u"""
        Attaches a guessed DocumentType to the Document object.
        
        The check for id is a standard way to determine whether the object
        is created (no row in the database yet, hence no id) or updated.
        """
        if not self.id:
            self.type = DocumentType.type_for_file(self.file)
        super(Document, self).save(*args, **kwargs)

    def get_size(self):
        return self.file.size
