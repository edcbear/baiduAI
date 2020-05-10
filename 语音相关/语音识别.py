# date : 2020/4/28 20:09     

from aip import AipSpeech
import os

""" 你的 APPID AK SK """
APP_ID = '19648874'
API_KEY = 'Pxmoii1MZQTYMj9iXK0fsPXt'
SECRET_KEY = '1LgCkoHIBlStvNsPsmOFNVC4G5ter8Vd'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


# 读取文件
def get_file_content(filePath):
    os.system(f"ffmpeg -y  -i {filePath} -acodec pcm_s16le -f s16le -ac 1 -ar 16000 {filePath}.pcm")
    with open(f"{filePath}.pcm", 'rb') as fp:
        return fp.read()


# 识别本地文件
res = client.asr(get_file_content('audio.mp3'), 'pcm', 16000, {
    'dev_pid': 1537,
})


print(res)