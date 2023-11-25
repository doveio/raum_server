from django.contrib import admin
from . models import Status, AssetType, Element, DataType, Process, RelationshipType


class StatusAdmin(admin.ModelAdmin):
    list_display = ['code','label', 'modified_by', 'modified_at',]

class AssetTypeAdmin(admin.ModelAdmin):
    list_display = ['code','label', 'modified_by', 'modified_at',]

class ElementAdmin(admin.ModelAdmin):
    list_display = ['code','label', 'modified_by', 'modified_at',]

class DataTypeAdmin(admin.ModelAdmin):
    list_display = ['code','label', 'modified_by', 'modified_at',]

class ProcessAdmin(admin.ModelAdmin):
    list_display = ['code','label', 'modified_by', 'modified_at',]

class RelationshipTypeAdmin(admin.ModelAdmin):
    list_display = ['code','label', 'modified_by', 'modified_at',]


admin.site.register(Status, StatusAdmin)
admin.site.register(AssetType, AssetTypeAdmin)
admin.site.register(Element, ElementAdmin)
admin.site.register(DataType, DataTypeAdmin)
admin.site.register(Process, ProcessAdmin)
admin.site.register(RelationshipType, RelationshipTypeAdmin)