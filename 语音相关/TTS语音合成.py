# date : 2020/4/28 20:00     

from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '19648874'
API_KEY = 'Pxmoii1MZQTYMj9iXK0fsPXt'
SECRET_KEY = '1LgCkoHIBlStvNsPsmOFNVC4G5ter8Vd'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


result = client.synthesis('你吃饭了吗', 'zh', 1, {
    'vol': 5,
    'spd': 7,
    'pit': 7,
    'per': 4,
})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
# if not isinstance(result, dict):
#     with open('auido.mp3', 'wb') as f:
#         f.write(result)

with open('auido.mp3', 'wb') as f:
    f.write(result)



