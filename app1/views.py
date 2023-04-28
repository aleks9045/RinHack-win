from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.decorators import action
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

    @action(detail=False, methods=['post'])
    def downloaddelete(self, request):
        if request.data['delete'] == 'no':
            fp = request.data['fp']
            file_path = list(Files.objects.all().filter(fp=fp).values())
            res_dict = {}
            for i in file_path:
                for count, j in enumerate(i.values()):
                    if count == 2:
                        res_dict[j.split("/")[-1]] = 'http://190.115.29.135/media/' + j
            return Response({'response': res_dict})
        elif request.data['delete'] == 'yes':
            fp = request.data['fp']
            Files.objects.filter(fp=fp).delete()
            return Response({'response': 'done'})


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
