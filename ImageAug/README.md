# ImageAug

데이터 증강을 위해 사용하며 회전, 블러, 노이즈, 명도 조절, 채도 조절 등  
다양한 증강 기법을 함수로 구현해 목적에 맞게 선택하여 사용할 수 있습니다.  
이를 통해 다량의 데이터를 구할 수 있어 모델 학습이 용이한 측면이 있으며  
또한 편의점 환경에 맞게 밝기를 높이거나 회전 각도를 적절히 설정하는 등  
앱의 실제 사용 환경을 고려하여 함수의 파라미터를 설정할 수 있습니다.

* 사용 언어    
Python 3.x

* 사용 환경    
Mac, Window

* 사용 라이브러리    
imgaug, pascal-voc-writer, xml, files,  
os, cv2, numpy, tqdm

* 사용 라이브러리 설치 및 사용
```python
pip install files
pip install pascal-voc-writer
pip install imgaug
import xml.etree.ElementTree 
import os
import cv2
import numpy
import imgaug
from files import *
from os import listdir
from imgaug import augmenters
from tqdm import tqdm_notebook
from pascal_voc_writer import Writer
```

* 선정된 증강 기법  
(괄호 안의 영문명은 파일 내 함수명과 일치합니다.)  </br>
(파라미터 설명 등 자세한 사항은 파일 내 주석을 참고하시면 되겠습니다.)  </br></br>
회전(rotation), 블러(blur), 노이즈(noise),  
명도 조절(bright), 무작위 위치에 박스 생성(box),  
모션 블러(motion blur), 채도 조정(color),  
픽셀화(pixel), 선명도 조정(sharpness), 드롭아웃(dropout)  
<br><br>
---
![캡처2](https://user-images.githubusercontent.com/67620728/131684992-ca0b7a87-c22b-44ec-ba76-fbf93138c0e0.PNG)
