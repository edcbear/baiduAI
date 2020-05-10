# encoding:utf-8
import requests
from aip import AipSpeech
import base64
import os,shutil,time,random

APP_ID = '19648874'
API_KEY = 'Pxmoii1MZQTYMj9iXK0fsPXt'
SECRET_KEY = '1LgCkoHIBlStvNsPsmOFNVC4G5ter8Vd'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=Pxmoii1MZQTYMj9iXK0fsPXt&client_secret=1LgCkoHIBlStvNsPsmOFNVC4G5ter8Vd'


def look_up_faces(filename):

    poxys = [
        {"HTTP": "117.88.5.253:3000"},
        {"HTTPS": "115.219.105.8:8010"},
        {"HTTPS": "171.35.170.144:9999"},
        {"HTTPS": "115.219.109.194:8010"},
        {"HTTPS": "120.39.216.129:808"},
        {"HTTPS": "115.223.68.95:8010"},
        {"HTTP": "115.219.104.57:8010"},
        {"HTTP": "115.223.88.91:8010"},
        {"HTTP": "121.237.149.165:3000"}
    ]
    a = random.choice(poxys)
    print(a)
    for type_, port_ in a.items():

        headers = {'content-type': 'application/x-www-form-urlencoded'}

        request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"

        token_response = requests.get(host,headers=headers,proxies={type_: port_})

        if token_response:
            access_token = token_response.json().get('access_token')

        # 二进制方式打开图片文件

        f = open(filename, 'rb')
        img = base64.b64encode(f.read())
        # params = "{'image':"%s+",'image_type':'BASE64','face_field':'faceshape,facetype'}"%img
        params = {"image": img, 'image_type': 'BASE64', 'face_field': 'age,beauty'}
        access_token = access_token
        request_url = request_url + "?access_token=" + access_token



        response = requests.post(request_url, data=params, headers=headers,proxies={type_: port_})

        if response:
            beauty = response.json().get('result').get('face_list')[0].get('beauty')
        beauty_girls = './beauty'
        notbeauty_girls = './notbeauty'

        if not os.path.exists(beauty_girls):
            os.makedirs(beauty_girls) # 创建路径
        if not os.path.exists(notbeauty_girls):
            os.makedirs(notbeauty_girls)  # 创建路径

        new_filename = filename.split('/')[-1]

        if beauty > 80:
            shutil.copyfile(filename, f"{beauty_girls}/{new_filename}")  # 复制文件
        else:
            shutil.copyfile(filename, f"{notbeauty_girls}/{new_filename}")

        time.sleep(3)

for filename in os.listdir("faces"):
    print(filename)
    look_up_faces(f'./faces/{filename}')

