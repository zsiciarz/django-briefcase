# -*- coding: utf-8 -*-

from django.contrib import admin
from briefcase.models import DocumentStatus, Document


class DocumentStatusAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'status', 'added_by', 'added_at', 'updated_at',)
    list_display_links = ('__unicode__',)


admin.site.register(DocumentStatus, DocumentStatusAdmin)
admin.site.register(Document, DocumentAdmin)
