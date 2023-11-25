from rest_framework import generics
from . import models
from . import serializers
# Create your views here.


class StatusList(generics.ListAPIView):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer

class StatusDetail(generics.RetrieveAPIView):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer

class AssetTypeList(generics.ListAPIView):
    queryset = models.AssetType.objects.all()
    serializer_class = serializers.AssetTypeSerializer

class AssetTypeDetail(generics.RetrieveAPIView):
    queryset = models.AssetType.objects.all()
    serializer_class = serializers.AssetTypeSerializer

class ProcessList(generics.ListAPIView):
    queryset = models.Process.objects.all()
    serializer_class = serializers.ProcessSerializer

class ProcessDetail(generics.RetrieveAPIView):
    queryset = models.Process.objects.all()
    serializer_class = serializers.ProcessSerializer

class ElementList(generics.ListAPIView):
    queryset = models.Element.objects.all()
    serializer_class = serializers.ElementSerializer

class ElementDetail(generics.RetrieveAPIView):
    queryset = models.Element.objects.all()
    serializer_class = serializers.ElementSerializer

class DataTypeList(generics.ListAPIView):
    queryset = models.DataType.objects.all()
    serializer_class = serializers.DataTypeSerializer

class DataTypeDetail(generics.RetrieveAPIView):
    queryset = models.DataType.objects.all()
    serializer_class = serializers.DataTypeSerializer