# GoodToSee TTS

- TTS 모듈 및 온라인 배포를 위한 API입니다.

## Requirements
### Environments
Python==3.7+<br>
Cuda==10.1<br>
CuDNN==7.6.5<br>
Tensorflow==2.3/2.4/2.5/2.6<br>
Tensorflow Addons >= 0.10.0<br>

### Modules
fastapi==0.68.1<br>
german-transliterate==0.1.3<br>
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
tensorflow==2.4.0<br>
tqdm==4.62.2<br>
uvicorn==0.15.0<br>

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
|&nbsp;&nbsp;&nbsp;&nbsp;| [losses]/: 오차 측정, 순전파, 역전파에 관련된 클래스와 메소드 보관.<br>
|&nbsp;&nbsp;&nbsp;&nbsp;| [models]/: 구현된 딥러닝 모델 보관.<br>
|&nbsp;&nbsp;&nbsp;&nbsp;| [optimizers]/: 최적화 함수 보관.<br>
|&nbsp;&nbsp;&nbsp;&nbsp;| [processor]/: dataset별 전처리를 수행할 코드 보관. 새로운 데이터셋으로 훈련을 진행할 경우, 해당 폴더의 하위 디렉토리 구조를 참고하여 새 폴더를 생성 후 유사한 전처리 코드를 .py로 구현해야 합니다.<br>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| [pretrained]/: 각 dataset별 정수 인코딩에 필요한 mapper 파일(.json) 보관.<br>
|&nbsp;&nbsp;&nbsp;&nbsp;| [trainers]/: 모델별 훈련을 진행할 코드 보관.<br>
|&nbsp;&nbsp;&nbsp;&nbsp;| [utils]/: 한국어 사전, decoder, griffin_lim vocoder 등 추가 유틸리티 보관.<br>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| - main.py: TTS syntehsizer + FastAPI server. (TTS의 경우, huggingface에 저장된 pre-trained model을 웹을 통해 불러와 합성을 진행합니다)<br>
<br>
NOTE: 훈련 시 활용할 음성파일 폴더의 세부 구조는 다음 링크를 참조하세요(https://github.com/crux153/TensorflowTTS). 전처리를 거친 후에는 하위폴더 [dump_] 내에 훈련할 .wav 파일이 .npy로 변환되어 저장됩니다.
