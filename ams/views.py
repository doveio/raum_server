from rest_framework import generics
from . import models
from . import serializers
from rest_framework.permissions import DjangoModelPermissions
# Create your views here.

class AssetList(generics.ListAPIView):
    queryset = models.Asset.objects.all()
    serializer_class = serializers.AssetSerializer

class AssetDetail(generics.RetrieveAPIView):
    queryset = models.Asset.objects.all()
    serializer_class = serializers.AssetSerializer

class BundleList(generics.ListCreateAPIView):
    queryset = models.Bundle.objects.all()
    serializer_class = serializers.BundleSerializer

class BundleDetail(generics.RetrieveDestroyAPIView):
    queryset = models.Bundle.objects.all()
    serializer_class = serializers.BundleSerializer

class ProductList(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

class ProductDetail(generics.RetrieveAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer