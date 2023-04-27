import hashlib
import json
from .models import UserUser, Files


def main_algorithm(new, old):
    new = str(new).replace("'", '"').replace('True', 'true').replace('False', 'false')
    jsn = json.loads(new)
    stroka = ''
    for iterator in jsn:
        stroka += str(jsn[iterator]['value'])
    hsh = hashlib.sha3_512(stroka.encode('utf-8')).hexdigest()
    for i in old:
        if i['fp'] == hsh:
            user_data = list(UserUser.objects.all().filter(fp=hsh).values('username', 'email'))
            files_data = list(Files.objects.all().filter(email=user_data[0]['email']).values().all())
            return [True, user_data, files_data]
    return [False, hsh]