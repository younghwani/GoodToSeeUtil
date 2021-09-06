# GoodToSee TTS

- TTS 모듈 및 온라인 배포를 위한 API입니다.

## How to Use
1) Python 3.6+ 이상 가상환경 생성
2) /tts 폴더에서 pip install -r requirements.txt 실행
2) IDE 등을 이용하여 main.py 파일 실행
3) localhost:5000에 접속해서 시연

## Requirements
### Environments
Python==3.6+<br>
Cuda==10.1<br>
CuDNN==7.6.5<br>
Tensorflow==2.3/2.4/2.5/2.6<br>
Tensorflow Addons >= 0.10.0<br>

* Tensorflow와 Tensorflow Addons는 서로 호환되는 버전이어야 합니다. 예컨대, Python 3.6에서 cudatoolkit==11.3, tensorflow==2.3이 설치되어 있을 경우, tensorflow-addons==0.12.1을 설치하기를 권장합니다. 버전 호환표는 다음 페이지를 참고하세요: https://github.com/tensorflow/addons<br>

### Modules
fastapi==0.68.1<br>
german-transliterate==0.1.3<br>
h5py==2.10<br>
inflect==5.3.0<br>
jamo==0.4.1<br>
jinja2==3.0.1<br>
librosa==0.8.1<br>
nltk==3.6.2<br>
num2words==0.5.10<br>
numpy==1.19.5<br>
pypinyin==0.42.0<br>
scikit-learn==0.24.2<br>
scipy==1.4.1<br>
SoundFile==0.10.3<br>
tqdm==4.62.2<br>
unidecode==1.2.0<br>
uvicorn==0.15.0<br>

* german-transliterate는 다음 코드를 사용하여 설치합니다: !pip install git+https://github.com/repodiac/german_transliterate<br>


## Folders
| [static]/: 생성된 오디오(.wav) 파일을 보관. (음성합성이 새로 이루어질 때마다 기존 파일을 덮어씌워 저장합니다)<br>
| [templates]/: 서버 웹페이지 템플릿을 보관.<br>
| [tensorflow_tts]/: 딥러닝 및 음성합성에 사용할 TensorflowTTS. Forked from https://github.com/crux153/TensorflowTTS<br>
|&nbsp;&nbsp;&nbsp;&nbsp;| [bin]/: 언어별로 음성/텍스트를 전처리하는 코드 보관.<br>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| - preprocess.py: 전처리기. processor 폴더 내의 전처리 코드들과 연동되어 있습니다.<br>
|&nbsp;&nbsp;&nbsp;&nbsp;| [configs]/: 각 모델별 hyperparameter 값을 보관.<br>
|&nbsp;&nbsp;&nbsp;&nbsp;| [datasets]/: 훈련할 모델별 데이터셋 loader 소스코드를 보관.<br> 
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| - abstract_dataset.py: 원하는 학습모델에 맞게 코드를 수정하여 사용합니다.<br>
|&nbsp;&nbsp;&nbsp;&nbsp;| [inference]/: config, model, processor를 묶어서 모듈화한 코드 보관.<br>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| - auto_processor.py: 특정 데이터셋에 대해 구현된 전처리기들과, 글자별 상응하는 숫자의 mapper 설정을 가져오는 기능을 합니다. 해당 작업은 from_pretrained(cls, pretrained_path) 함수가 수행합니다.<br>
|&nbsp;&nbsp;&nbsp;&nbsp;| [losses]/: 오차 측정, 순전파, 역전파에 관련된 클래스와 메소드 보관.<br>
|&nbsp;&nbsp;&nbsp;&nbsp;| [models]/: 구현된 딥러닝 모델 보관.<br>
|&nbsp;&nbsp;&nbsp;&nbsp;| [optimizers]/: 최적화 함수 보관.<br>
|&nbsp;&nbsp;&nbsp;&nbsp;| [processor]/: 폴더 하부에 원하는 데이터셋의 Processor를 정의합니다. BaseProcessor(=base_processor.py)를 상속받아오고, 여기에 utils.py와 korean.py에 정의된 클래스를 import해 와서 각 데이터셋에 맞게 클래스를 구현합니다. 한국어로는 kss.py의 형태로 전처리기가 구현되어 있으므로, 이를 참고해 일부 변수의 값만 바꾸어 새로운 한국어 데이터셋의 전처리기를 구현할 수 있습니다. 만약 새로 추가된 데이터셋에 대한 프로세서가 있다면, 이 파일 내부에 추가해주어야 합니다.<br>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| [pretrained]/: 폴더 내에 데이터셋에 해당하는 mapper 파일을 준비합니다. 각 음소(철자)를 정수로 인코딩하는데 사용합니다. 현재 한국어로는 kss 데이터셋에 대한 kss_mapper, 영어로는 ljspeech 데이터셋에 대한 ljspeech_mapper를 지원합니다. 한국어의 경우 kss_mapper를 그대로 사용하거나, 일부 요소를 변경하여 사용합니다.<br>
|&nbsp;&nbsp;&nbsp;&nbsp;| [trainers]/: 모델별 훈련을 진행할 코드 보관.<br>
|&nbsp;&nbsp;&nbsp;&nbsp;| [utils]/: 한국어 처리기, decoder, griffin_lim vocoder 등 추가 유틸리티 보관.<br>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| - korean.py: 한국어 전처리기입니다. 특수한 문자열(영어약자, 숫자, 한자, 문장부호 등)을 한국어 문자열로 바꾸고, 해당 문자열을 음소로 풀어쓰기하기 위한 처리기가 정의되어 있습니다. 한국어 풀어쓰기는 jamo 라이브러리를 import해와서 구현합니다. 만약에 정의되어 있지 않은 key:value 페어가 있다면, 본 파일에 포함된 딕셔너리에 정의하면 됩니다.<br>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| - cleaners.py: 텍스트를 각 언어별 mapper.json에 정의된 범위 내의 텍스트로 바꾸는 과정을 실질적으로 수행합니다. 앞서 말씀드렸듯 한국어 tokenizer의 경우 korean.py로 저장되어 있으므로, 이를 import해와 사용합니다.<br>
|&nbsp;&nbsp;&nbsp;&nbsp;| - main.py: TTS syntehsizer + FastAPI server. (TTS의 경우, huggingface에 저장된 pre-trained model을 웹을 통해 불러와 합성을 진행합니다) 해당 파일을 실행하여 서버를 시작합니다.<br>
<br>
NOTE: 훈련 시 활용할 음성파일 폴더의 세부 구조는 다음 링크를 참조하세요(https://github.com/crux153/TensorflowTTS). 전처리를 거친 후에는 하위폴더 [dump_] 내에 훈련할 .wav 파일이 .npy로 변환되어 저장됩니다.
