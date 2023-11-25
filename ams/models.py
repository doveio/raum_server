from django.db import models

from core.models import RaumBaseClass, Element, AssetType, Process, DataType, RelationshipType

class Project(RaumBaseClass):
    label = models.CharField(max_length=64)
    code = models.CharField(max_length=64, unique=True)
    metadata = models.JSONField(null=True, blank=True)

class Asset(RaumBaseClass):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    asset_type = models.ForeignKey(AssetType, on_delete=models.PROTECT, default=1)
    code = models.CharField(max_length=64, unique=True)
    client_name = models.CharField(max_length=64, unique=True)
    frame_range = models.JSONField(null=True, blank=True)
    metadata = models.JSONField(null=True, blank=True)

    class Meta:
        unique_together = ('project', 'code')

    def __str__(self):
        return self.code

class Bundle(RaumBaseClass):

    asset = models.ForeignKey(Asset, on_delete=models.PROTECT, default=1)
    process = models.ForeignKey(Process, on_delete=models.PROTECT, default=1)
    element = models.ForeignKey(Element, on_delete=models.PROTECT, default=1)
    version = models.IntegerField(null=True, blank=True, default=0)
    metadata = models.JSONField(null=True, blank=True)

    class Meta:
        unique_together = ('asset','process', 'element', 'version')
        
    def save(self, *args, **kwargs):
        '''
        Custom save implemented to make sure there is a automatic version 
        increamentation done if no version provided when creating the model
        '''
        if not self.version:
            try:
                existing_instance = Bundle.objects.filter(
                                                    process=self.process,
                                                    element = self.element,
                                                    asset = self.asset
                                                    ).order_by('-id')[0]
                next_version = existing_instance.version + 1
                self.version = next_version
            except IndexError:
                self.version = 1

        super(Bundle, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.id}-{self.asset}/{self.process}/{self.element}/{self.version}'

class Product(RaumBaseClass):
    bundle = models.ForeignKey(Bundle, on_delete=models.CASCADE)
    data_type = models.ForeignKey(DataType, on_delete=models.PROTECT, default=1)
    filepath = models.CharField(max_length=1024, unique=True)
    extension = models.CharField(max_length=8)
    frame_range = models.JSONField(null=True, blank=True)
    version = models.IntegerField(null=True, blank=True, default=0)
    metadata = models.JSONField(null=True, blank=True)

    def save(self, *args, **kwargs):
        '''
        Custom save implemented to make sure there is a automatic version 
        increamentation done if no version provided when creating the model
        '''
        if not self.version:
            try:
                existing_instance = Product.objects.filter(
                                                    bundle=self.bundle,
                                                    data_type = self.data_type,
                                                    ).order_by('-id')[0]
                next_version = existing_instance.version + 1
                self.version = next_version
            except IndexError:
                self.version = 1

        super(Product, self).save(*args, **kwargs)

class AssetHierarchy(RaumBaseClass):
    class Meta:
        unique_together = ('asset','relationship')
        verbose_name_plural = 'AssetHierarchies'

    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    relationship = models.ForeignKey(RelationshipType, on_delete=models.PROTECT)
    connections = models.ManyToManyField(Asset, related_name='%(class)s_connection')


class ProductDependency(RaumBaseClass):
    product = models.OneToOneField(Asset, on_delete=models.CASCADE)
    connections = models.ManyToManyField(Asset, related_name='%(class)s_connection')
    class Meta:
        verbose_name_plural = 'ProductDependencies'