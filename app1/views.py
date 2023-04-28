from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.parsers import FormParser, MultiPartParser
from .serializers import Files_Serialaizer
from .models import Files, Hshs, UserUser
from .algorithms import main_algorithm


class UserUserView(APIView):
    def get(self, request):
        lst = UserUser.objects.all().values()
        return Response({'response': list(lst)})

    def post(self, request):
        fp = request.data['fp']
        UserUser.objects.filter(fp=fp).delete()
        new_post = UserUser.objects.create(
            fp=fp,
            username=request.data['username']
        )
        return Response({'response': model_to_dict(new_post)})


class FileUploadViewSet(ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = Files_Serialaizer
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        serializer.save(file=self.request.data.get('file'))

    @action(detail=False, methods=['post'])
    def download(self, request):
        fp = request.data['fp']
        file_path = list(Files.objects.all().filter(fp=fp).values())
        file_paths = []
        print(file_path)
        for i in file_path:
            for count, j in enumerate(i.values()):
                if count == 2:
                    file_paths.append('http://127.0.0.1:8000/media/' + j)
        return Response({'response': file_paths})


class UserDataView(APIView):
    def get(self, request):
        lst = Hshs.objects.all().values()
        return Response({'response': list(lst)})

    def post(self, request):
        new_data = request.data['fp']
        old_data = Hshs.objects.all().values()
        res = main_algorithm(new_data, list(old_data))
        if res[0]:
            return Response({'user': res[1], 'files': res[2]})
        else:
            new_post = Hshs.objects.create(
                fp=res[1]
            )
            return Response({'response': model_to_dict(new_post)})
