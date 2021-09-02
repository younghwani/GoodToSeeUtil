# 시각장애인을 위한 편의점 특화 상품인식 서비스 개발

- 데이터청년캠퍼스 한국외국어대학교 과정
- Team : GoodToSee

## 발표자료 및 시연영상
- 발표자료 : https://github.com/younghwani/GoodToSeeUtil/blob/master/GoodToSee_ppt.pdf
- 시연영상 : https://github.com/younghwani/GoodToSeeUtil/blob/master/GoodToSee_demo.MP4

## 이미지 전처리
1. ImageScrap : 크롬드라이버와 selenium을 활용해 이미지를 스크랩(크롤링)합니다.
2. ImageGathering : 데이터 수집 및 전처리 과정에 이용합니다. 직접 영상을 촬영하여 프레임별 이미지를 추출한 후 라벨링에 사용합니다.
3. ImageRename : 라벨링과 협업 과정에서 데이터 파악의 용이함을 위해 상품명으로 파일명을 통일합니다.
4. ImageAug : 수집 및 라벨링 과정을 거친 raw 데이터 증강을 위해 사용합니다.

## TTS engine
- 환경설정, 모듈 구성 등 자세한 설명은 GoodToSeeUtil/tts 디렉토리에서 확인하실 수 있습니다.
1. FastAPI : request 입력 시 합성된 음성 파일을 전달하는 구성을 갖습니다.
2. Tensorflow
3. Pre-trained FastSpeech2
