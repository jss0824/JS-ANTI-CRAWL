# -*- coding: utf-8 -*-
# coder : Jay
import requests
import execjs
import json

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
}

url = 'https://c13.shuqireader.com/pcapi/chapter/contentfree/?bookId=6813923&chapterId=674174&ut=1472714703&num=1&ver=1&aut=1563255851&sign=c6b551c7f510d444fef749167e25b835'

res = requests.get(url,headers=header)
content = json.loads(res.text)['ChapterContent']
print(content)

with open('G:/JS-example/阿里文学/demo.js', 'r', encoding='utf-8') as f:
    ctx = execjs.compile(f.read())
    js = 'decode_con("{}")'.format(content)
    value = ctx.eval(js)
    print(value)


