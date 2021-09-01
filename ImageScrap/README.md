# ImageScrap

이 파일은 상품 이미지 데이터를 구글에서 크롤링할 때 사용합니다. 원하는 검색어를 Input으로 지정하시고 이미지를 저장할 경로를 지정하시면 크롤링이 자동으로 진행됩니다.    
크롬을 이용하기 때문에 크롬드라이버의 별도 설치가 필요하며 크롬 드라이버는 본인의 운영체제와 크롬 버전을 확인하여 다운 받으셔야 합니다.    
[크롬드라이버 설치](https://chromedriver.chromium.org/)    
[크롬 버전 확인](https://mainia.tistory.com/2616)

* 사용 언어    
Python

* 사용 환경    
Mac, Window

* 사용 라이브러리 설치 및 로드

```
pip install beautifulsoup4
pip install selenium
```
```python
from urllib.request import urlopen
from urllib.request import urlretrieve
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import os
```
