from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from .serializers import Files_Serialaizer
from .models import Files


class Files_ViewSet(ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = Files_Serialaizer
    permission_classes = (AllowAny,)

