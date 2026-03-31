import pyaudio
import json
from vosk import Model, KaldiRecognizer

# 1. 加载模型
MODEL_PATH = "model"
model = Model(MODEL_PATH)

# 2. 配置音频参数（Vosk要求16kHz单声道）
SAMPLERATE = 16000
CHUNK = 4000  # 每次读取的音频帧大小

# 3. 初始化识别器
rec = KaldiRecognizer(model, SAMPLERATE)

# 4. 初始化麦克风
p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=SAMPLERATE,
    input=True,
    frames_per_buffer=CHUNK
)

# 5. 开始实时识别
stream.start_stream()
print("麦克风实时识别已启动（按Ctrl+C停止）...\n")

try:
    while True:
        data = stream.read(CHUNK)
        if rec.AcceptWaveform(data):
            # 输出完整句子识别结果
            result = json.loads(rec.Result())
            if result["text"]:
                print(f"识别结果：{result['text']}")
        else:
            # 输出部分识别结果（实时预览）
            partial = json.loads(rec.PartialResult())
            if partial["partial"]:
                print(f"实时预览：{partial['partial']}", end="\r")
except KeyboardInterrupt:
    print("\n\n识别已停止")
finally:
    # 释放资源
    stream.stop_stream()
    stream.close()
    p.terminate()
