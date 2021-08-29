# --->
# Created by liumeiyu on 2021/8/27.
# '_'

import requests
from requests import RequestException
from bs4 import BeautifulSoup
from multiprocessing import Pool


login_url = ''
baidu_news = 'https://www.zhihu.com/question/22855572'

header = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}
data = {'users': 'abc', 'password': '123'}  # 密码登录
form_data = {
    'source': 'index_nav',
    'form_email': 'xxx',
    'form_password': 'xxx',
    'captcha-solution': 'stamp',
    'captcha-id': 'b3dssX515MsmNaklBX8uh5Ab:en'
}


def get_req():
    try:
        r = requests.get(url=baidu_news, headers=header)
        r.encoding = 'utf-8'
        if r.status_code == 200:
            return r.text  # h5页面  r.json()
        return None
    except RequestException:
        print("request_err")
        return None


def get_req_with_password():
    sess = requests.session()
    response = sess.post(url=login_url, headers=header, data=data)
    if response.status_code == 200:
        response = sess.get(url=baidu_news, headers=header)
        if response.status_code == 200:
            return response.text


def extra_html(html):
    soup = BeautifulSoup(html, 'lxml')
    # print(soup.prettify())
    print(soup.title)
    print(soup.head.contents)
    print(soup.head.attrs)


def main():
    html5 = get_req()
    extra_html(html5)


if __name__ == '__main__':
    main()
    # p = Pool()
    # p.map(main, [i * 10 for i in range(10)])



