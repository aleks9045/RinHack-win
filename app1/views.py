from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import Files_Serialaizer
from .models import Files, UserData
from .algorithms import main_algorithm


class Files_ViewSet(ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = Files_Serialaizer
    permission_classes = (AllowAny,)


class UserDataView(APIView):
    def get(self, request):
        lst = UserData.objects.all().values()
        return Response({'response': list(lst)})

    def post(self, request):
        new_post = UserData.objects.create(
            ip=request.data['ip'],
            lang=request.data['lang'],
            all_lang=request.data['all_lang'],
            fp=request.data['fp'],
            display=request.data['display'],
            cords=request.data['cords']
        )
        old_posts = UserData.objects.all().values()
        main_algorithm(model_to_dict(new_post), old_posts)
        return Response({'response': model_to_dict(new_post)})