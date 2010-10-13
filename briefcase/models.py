# -*- coding: utf-8 -*-

import os
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


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


class Document(models.Model):
    u"""
    The document itself.
    """
    # Basic document data.
    file = models.FileField(verbose_name=_("file"), upload_to='uploads/%Y/%m/%d/', help_text=_("This is the document itself - well, just a file."))

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
