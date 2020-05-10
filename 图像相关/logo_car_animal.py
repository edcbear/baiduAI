# encoding:utf-8
import requests
from aip import AipSpeech
import base64

APP_ID = '19648874'
API_KEY = 'Pxmoii1MZQTYMj9iXK0fsPXt'
SECRET_KEY = '1LgCkoHIBlStvNsPsmOFNVC4G5ter8Vd'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=Pxmoii1MZQTYMj9iXK0fsPXt&client_secret=1LgCkoHIBlStvNsPsmOFNVC4G5ter8Vd'
response = requests.get(host)
if response:
    print(response.json().get('access_token'))
    access_token = response.json().get('access_token')


'''
车型识别
'''

request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/car"
# 二进制方式打开图片文件
f = open('./cars/class.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"image":img,"top_num":5,"baike_num":2}
access_token = access_token
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
body = {

}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print(response.json().get('result')[0].get('name'),response.json().get('result')[0].get('year'))

