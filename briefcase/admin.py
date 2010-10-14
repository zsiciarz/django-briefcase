# -*- coding: utf-8 -*-

from django.contrib import admin
from briefcase.models import DocumentStatus, DocumentType, Document


class DocumentStatusAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class DocumentTypeAdmin(admin.ModelAdmin):
    pass


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'type', 'status', 'added_by', 'added_at', 'updated_at',)
    list_display_links = ('__unicode__',)
    list_filter = ('type', 'status',)
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.added_by = request.user
        super(DocumentAdmin, self).save_model(request, obj, form, change)


admin.site.register(DocumentStatus, DocumentStatusAdmin)
admin.site.register(DocumentType, DocumentTypeAdmin)
admin.site.register(Document, DocumentAdmin)
