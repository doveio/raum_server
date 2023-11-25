from django.contrib import admin
from . models import Project, Asset, Bundle, Product, AssetHierarchy, ProductDependency


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['label','code','modified_by', 'modified_at',]

class AssetAdmin(admin.ModelAdmin):
    list_display = ['code','asset_type','client_name', 'modified_by', 'modified_at',]
    list_filter = ["asset_type"]

class BundleAdmin(admin.ModelAdmin):
    list_display = ['version','process','element','asset','modified_by', 'modified_at',]
    list_filter = ['process', 'element',]
    search_fields = ['process__label', 'element__label', 'asset__code']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['filepath','version','frame_range','extension', 'modified_by', 'modified_at', 'bundle']


class AssetHierarchyAdmin(admin.ModelAdmin):
    list_display = ['asset', 'relationship', 'get_connections']

    def get_connections(self,obj):
        return [connection.code for connection in obj.connections.all()]
    

class ProductDependencyAdmin(admin.ModelAdmin):
    list_display = ['product', 'get_connections']

    def get_connections(self,obj):
        return [connection.code for connection in obj.connections.all()]


admin.site.register(ProductDependency, ProductDependencyAdmin)
admin.site.register(AssetHierarchy, AssetHierarchyAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Asset, AssetAdmin)
admin.site.register(Bundle, BundleAdmin)
admin.site.register(Product, ProductAdmin)