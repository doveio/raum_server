from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model=User
    # fields = '__all__'
    fields = ('id','username', 'email')

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Status
        fields = ('id','code', 'label')

class AssetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AssetType
        fields = ('id','code', 'label')

class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Process
        fields = ('id','code', 'label')

class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Element
        fields = ('id','code', 'label')

class DataTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DataType
        fields = ('id','code', 'label')