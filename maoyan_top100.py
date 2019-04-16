import csv
import json
import re

import requests
from requests import RequestException


# 发送请求，获取响应
def get_url(url):
    try:
        header = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36" }
        res = requests.get(url, header)
        res.encoding = res.apparent_encoding
        if res.status_code == 200:
            return res.text
    except RequestException:
        pass


# 解析响应
def parse_html(html):
    pattern = re.compile('<dd>.*?board-index.*?">(\d+)</i>'
                         + '.*?data-src="(.*?)".*?'
                         + '.*?class="name"><a.*?title="(.*?)"'
                         + '.*?class="star">(.*?)</p>'
                         + '.*?class="releasetime">(.*?)</p>    </div>'
                         + '.*?class="score">.*?integer">(.*?)</i>'
                         + '.*?class="fraction">(\d+)</i></p>.*?</dd>', re.S)
    terms = re.findall(pattern, html)
    content = []
    for term in terms:
        content.append(
            dict(index=term[0], image=term[1], title=term[2], actor=term[3], time=term[4], score=term[5] + term[6])
        )
    return content


# 保持数据
def write_tofile(content):
    # 存为JSON文件
    # for item in content:
    #     with open('result_json.txt', 'a', encoding='utf-8') as fo:
    #         fo.write(json.dumps(item, ensure_ascii=False) + '\n')

    # 存为CSV格式
    for item in content:
        with open('result_csv.csv', 'a', newline='', encoding='ANSI') as fo:
            writer = csv.writer(fo)
            writer.writerow([item['index'], item['image'], item['title'], item['actor'], item['time'], item['score']])


if __name__ == "__main__":

    with open('result_csv.csv', 'a', newline='', encoding='ANSI') as fo:
        writer = csv.writer(fo)
        writer.writerow(['排名', '图片', '电影名称', '主演', '上映时间', '评分'])

    for i in range(10):
        url = 'https://maoyan.com/board/4?offset=' + str(i * 10)
        # print(url)
        html = get_url(url)
        # print(html)
        content = parse_html(html)
        write_tofile(content)
