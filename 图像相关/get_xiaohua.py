# date : 2020/4/29 9:43     

import os
import time

import requests
from lxml import etree

host = "http://www.xueshengmai.com"

headers = {
    'User-Agent': '"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

for i in range(0,10):
    xiaohua_res = requests.get(f'http://www.xueshengmai.com/list-1-{i}.html').text

    xiaohua_imgs = etree.HTML(xiaohua_res).xpath('//*[@id="list_img"]//a/img')
    for img in xiaohua_imgs:

        url = img.xpath('@src')[0]
        title = img.xpath('@alt')[0]
        print(host+str(url))
        if str(url).startswith('h'):
            img_content = requests.get(url).content
        else:
            img_content = requests.get(host+str(url), headers=headers).content

        img_path = os.path.join("faces", f"{title}.jpg")

        with open(img_path, 'wb') as f:
            f.write(img_content)

        time.sleep(0.1)











