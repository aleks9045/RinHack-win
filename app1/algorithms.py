import hashlib
import json
from .models import UserUser, Files


def main_algorithm(new, old):
    try:
        jsn = json.loads(str(new).replace("'", '"').replace('True', 'true').replace('False', 'false'))
        stroka = ''
        for iterator in jsn:
            stroka += str(jsn[iterator]['value'])
        hsh = hashlib.sha3_512(stroka.encode('utf-8')).hexdigest()
    except Exception as ex:
        hsh = new
    for i in old:
        if i['fp'] == hsh:
            if not list(UserUser.objects.all().values()):
                user_data = {'username': ''}
                files_data = ''
            elif not list(Files.objects.all().values()):
                user_data = list(UserUser.objects.all().filter(fp=hsh).values('username', 'fp'))
                files_data = ''
            else:
                user_data = list(UserUser.objects.all().filter(fp=hsh).values('username', 'fp'))
                files_data = list(Files.objects.all().filter(fp=user_data[0]['fp']).values().all())
            return [True, user_data, files_data]
    return [False, hsh]
