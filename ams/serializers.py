
from django.contrib.auth.models import User
from rest_framework import serializers
from . import models
from core.serializers import UserSerializer, ProcessSerializer, ElementSerializer, DataTypeSerializer


class AssetSerializer(serializers.ModelSerializer):
    # created_by = UserSerializer(read_only=True)
    # modified_by = UserSerializer(read_only=True)
    class Meta:
        model = models.Asset
        fields = ('id','code', 'asset_type', 'client_name', 'frame_range')

class BundleSerializer(serializers.ModelSerializer):
    asset = AssetSerializer(read_only=True)
    process = ProcessSerializer(read_only=True)
    element = ElementSerializer(read_only=True)
    data_type = DataTypeSerializer(read_only=True)
    
    class Meta:
        model = models.Bundle
        fields = ('id','asset', 'process', 'data_type', 'element', 'version')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ('id','filepath', 'frame_range', 'extension', 'bundle')
