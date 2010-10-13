# -*- coding: utf-8 -*-

from django.contrib import admin
from briefcase.models import DocumentStatus, Document


class DocumentStatusAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(DocumentStatus, DocumentStatusAdmin)
