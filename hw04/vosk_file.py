import wave
import json
from vosk import Model, KaldiRecognizer

# 1. 加载Vosk中文轻量模型（请确保model文件夹在同级目录）
MODEL_PATH = "model"
model = Model(MODEL_PATH)

# 2. 配置音频文件路径（替换为你的剪映配音音频路径）
AUDIO_PATH = "dubbing.wav"

# 3. 打开音频文件（要求：16kHz, 16位, 单声道wav格式）
wf = wave.open(AUDIO_PATH, "rb")
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    raise ValueError("音频必须为16kHz、16位、单声道的wav格式！")

# 4. 初始化识别器
rec = KaldiRecognizer(model, wf.getframerate())
rec.SetWords(True)  # 输出词级时间戳（可选）

# 5. 流式识别音频
print("开始识别音频文件...")
while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    rec.AcceptWaveform(data)

# 6. 输出最终结果
final_result = json.loads(rec.FinalResult())
print("\n识别结果：")
print(final_result["text"])

# 7. 输出带时间戳的词级结果（可选）
print("\n词级时间戳：")
for word in final_result.get("result", []):
    print(f"[{word['start']:.2f}s - {word['end']:.2f}s]: {word['word']}")
