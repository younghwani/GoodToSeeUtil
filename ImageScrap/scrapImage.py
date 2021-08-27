# 1. 활용 library
from urllib.request import urlopen
from urllib.request import urlretrieve
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import os

# 2. 검색어 입력
# search = input("검색어")

# ko_list = ['치토스', '칙촉', '카스타드', '칸쵸', '크런키빼빼로', '삼양짱구', '고래밥',
#         '꼬북칩콘스프', '눈을감자', '다이제오리지널', '도도한나쵸치즈', '오리온땅콩강정', '스윙칩고추장',
#         '스윙칩어니언', '오감자', '오뜨쇼콜라',
#            '사또밥', '고소미', '예감', '다이제초코']
# en_list = ['cheetos', 'chic_choc', 'custard', 'kancho', 'crunky_pepero', 'changgu', 'whale_rice',
#            'turtle_chips', 'eye_potato', 'diget', 'nacho_cheese', 'peanut_gangjeong', 'swingchip_hot',
#            'swingchip_onion', 'oh_potato', 'oddu',
#            'saddo_bob', 'kosomi', 'yeagam', 'diget_choco']

ko_list = ['사또밥', '고소미', '예감', '다이제초코']
en_list = ['saddo_bob', 'kosomi', 'yeagam', 'diget_choco']

for idx in range(len(ko_list)):
    url = f'https://www.google.com/search?q={quote_plus(ko_list[idx])}&sxsrf=ALeKk02QeiWfv6bCTCr7BF_BPHDuAyPmew:1594639559008&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiBiNajj8rqAhXCIqYKHcAECvgQ_AUoAXoECBQQAw&biw=1536&bih=722'

    # 3. 이미지 수집
    driver = webdriver.Chrome()
    driver.get(url)
    for i in range(300):
        driver.execute_script("window.scrollBy(0,10000)")

    html = driver.page_source
    soup = BeautifulSoup(html)
    img = soup.select('img')
    n = 1
    imgurl = []

    for i in img:
        try:
            imgurl.append(i.attrs["src"])
        except KeyError:
            imgurl.append(i.attrs["data-src"])

    for i in imgurl:
        urlretrieve(i, "/Users/kyh/GitHub/ImageScrap/" + en_list[idx] + "/" + en_list[idx] + str(n) + ".jpg")
        n += 1
    driver.close()