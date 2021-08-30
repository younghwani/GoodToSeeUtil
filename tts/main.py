# from flask import Flask, render_template, request, Response, send_from_directory
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.templating import Jinja2Templates
import uvicorn

import numpy as np
import soundfile as sf
import yaml
import time

import tensorflow as tf

from tensorflow_tts.inference import AutoConfig
from tensorflow_tts.inference import TFAutoModel
from tensorflow_tts.inference import AutoProcessor

# initialize fastspeech model (Korean)
fs_config_ko = AutoConfig.from_pretrained('tensorspeech/tts-fastspeech2-kss-ko')
fastspeech_ko = TFAutoModel.from_pretrained(
    config=fs_config_ko,
    pretrained_path="tensorspeech/tts-fastspeech2-kss-ko"
)

# initialize fastspeech model (English)
fs_config_en = AutoConfig.from_pretrained('tensorspeech/tts-fastspeech2-ljspeech-en')
fastspeech_en = TFAutoModel.from_pretrained(
    config=fs_config_en,
    pretrained_path="tensorspeech/tts-fastspeech2-ljspeech-en"
)

# initialize melgan model (Korean)
melgan_config_ko = AutoConfig.from_pretrained('tensorspeech/tts-mb_melgan-kss-ko')
melgan_ko = TFAutoModel.from_pretrained(
    config=melgan_config_ko,
    pretrained_path="tensorspeech/tts-mb_melgan-kss-ko"
)

# initialize melgan model (Korean)
melgan_config_en = AutoConfig.from_pretrained('tensorspeech/tts-mb_melgan-ljspeech-en')
melgan_en = TFAutoModel.from_pretrained(
    config=melgan_config_en,
    pretrained_path="tensorspeech/tts-mb_melgan-ljspeech-en"
)

# inference
def synthesize(input_lang, input_txt, input_rate=1.0, input_freq=1.0):
    if input_lang == 0:
        path = "tensorspeech/tts-fastspeech2-kss-ko"
        fastspeech = fastspeech_ko
        melgan = melgan_ko

    elif input_lang == 1:
        path = "tensorspeech/tts-fastspeech-ljspeech-en"
        fastspeech = fastspeech_en
        melgan = melgan_en

    processor = AutoProcessor.from_pretrained(pretrained_path=path)

    ids = processor.text_to_sequence(input_txt)
    ids = tf.expand_dims(ids, 0)

    # fastspeech inference
    masked_mel_before, masked_mel_after, duration_outputs, _, _ = fastspeech.inference(
        input_ids=ids,
        speaker_ids=tf.convert_to_tensor([0], dtype=tf.int32),
        speed_ratios=tf.convert_to_tensor([input_rate], dtype=tf.float32),
        f0_ratios=tf.convert_to_tensor([input_freq], dtype=tf.float32),
        energy_ratios=tf.convert_to_tensor([1.0], dtype=tf.float32),
    )

    # melgan inference
    audio_after = melgan.inference(masked_mel_after)[0, :, 0]

    return audio_after

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    response = await call_next(request)
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache, no-store'
    response.headers['Expires'] = '0'
    return response

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    data = {
        "page": "home page"
    }
    return templates.TemplateResponse("simple.html", {"request": request, "data": data})

@app.post("/static/audio.wav", response_class=JSONResponse)
async def audio_synth(request: Request):
    result = await request.form()
    txt = result['speech']
    lang = int(result['switch'])
    rate = float(result['rate'])
    freq = float(result['freq'])

    print(txt, lang, rate, freq)

    audio_after = synthesize(lang, txt, rate, freq)
    sf.write('./static/audio.wav', audio_after, 22050)

    return JSONResponse(status_code=200, content={"result": "success"})

# FastAPI
@app.get("/static/audio.wav", response_class=FileResponse)
async def audio_get():
    path_to_file = "./static/audio.wav"
    return FileResponse(path_to_file, media_type="audio/wav")

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=5000)

# if __name__ == '__main__':
#     app.run('0.0.0.0', port=5000, debug=True)
