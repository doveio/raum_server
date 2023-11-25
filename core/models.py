from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet

# Create your models here.

class RaumBaseClass(models.Model):
    '''
    Base class to inherit basic properties
    '''
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='%(class)s_created_by', null=True, blank=True)
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='%(class)s_modified_by', null=True, blank=True)
    active = models.BooleanField(default=True)

    # objects = models.Manager()


class Status(RaumBaseClass):
    '''
    Status model
    '''
    class Meta:
        verbose_name_plural = 'Statuses'
        ordering = ('label',)

    label = models.CharField(max_length=32)
    code = models.CharField(max_length=12, unique=True)   

    def __str__(self):
        return self.label
    

class AssetType(RaumBaseClass):
    '''
    Asset Types model, for eg: character, ennironment, shot, picture in picture etc
    '''
    class Meta:
        ordering = ('label',)

    label = models.CharField(max_length=32)
    code = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return self.label



class Element(RaumBaseClass):
    '''
    Elements like anim_geo_cache, anim
    '''
    class Meta:
        ordering = ('label',)
    
    label = models.CharField(max_length=32)
    code = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return self.label


class Process(RaumBaseClass):
    '''
    Elements like anim_geo_cache, anim
    '''
    class Meta:
        verbose_name_plural = 'Processes'
        ordering = ('label',)

    label = models.CharField(max_length=32)
    code = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return self.label
    

class DataType(RaumBaseClass):
    '''
    Elements like anim_geo_cache, anim
    '''
    class Meta:
        ordering = ('label',)

    label = models.CharField(max_length=32)
    code = models.CharField(max_length=12, unique=True)
    
    def __str__(self):
        return self.label
    
class RelationshipType(RaumBaseClass):
    '''
    Elements like anim_geo_cache, anim
    '''
    class Meta:
        ordering = ('label',)

    label = models.CharField(max_length=32)
    code = models.CharField(max_length=12, unique=True)
    
    def __str__(self):
        return self.label