# vioce-recognition
## 一、目录结构
hw04/├── README.md # 本文件：总览与运行说明├── text_gen.md # 任务一：大模型文本生成├── jianying.md # 任务二：剪映 AI 音色克隆说明├── asr_report.md # 任务三：ASR 方案调研与实现报告├── experiment_log.md # 任务三：ASR 实验记录├── requirements.txt # ASR 代码依赖├── vosk_file.py # ASR 音频文件识别代码├── vosk_realtime.py # ASR 麦克风实时识别代码├── model/ # Vosk 中文轻量模型（需自行下载）└── assets/ # 测试音频 / 视频└── dubbing.wav # 剪映导出的配音音频
plaintext

## 二、各任务对应文件
| 任务 | 对应文件 | 说明 |
|------|----------|------|
| 任务一 | `text_gen.md` | 大模型生成文本、模型与Prompt说明 |
| 任务二 | `jianying.md` | 剪映AI音色克隆步骤、导出格式、网盘链接 |
| 任务三 | `asr_report.md` `experiment_log.md` `vosk_file.py` `vosk_realtime.py` | ASR方案对比、代码、实验结果 |

## 三、任务二：剪映产出说明
### 1. 克隆步骤概要
1.  打开剪映PC版，新建项目，导入参考视频
2.  新建测试文本，使用「AI克隆」功能录制本人声音，完成音色克隆并保存
3.  导入大模型生成的文案，添加为视频文本，选择克隆音色进行文本朗读
4.  导出为MP4格式视频，上传至夸克网盘

### 2. 导出文件格式
- 格式：MP4，H.264编码，1080p分辨率，30fps
- 音频：48kHz采样率，AAC编码

### 3. 资源链接
夸克网盘链接：https://pan.quark.cn/s/0f976cb6ad42
提取方式：复制链接打开「夸克APP」即可获取

## 四、任务三：ASR代码运行说明
### 1. 环境准备
1.  安装Python 3.8+
2.  安装依赖：
```bash
pip install -r requirements.txt
下载 Vosk 中文轻量模型：https://alphacephei.com/vosk/models
选择vosk-model-small-cn-0.22，解压后将文件夹重命名为model，放入hw04目录下
准备剪映导出的配音音频，命名为dubbing.wav，放入assets目录
2. 运行代码
（1）音频文件识别（剪映配音）
bash
运行
python vosk_file.py
（2）麦克风实时识别
bash
运行
python vosk_realtime.py
3. 注意事项
音频文件必须为16kHz、16 位、单声道的 wav 格式，否则无法识别
实时识别需确保麦克风正常工作，无严重背景噪声
若需提升准确率，可更换为大模型vosk-model-cn-0.22
五、提交检查清单
✅ 任务一：text_gen.md 完整✅ 任务二：jianying.md 步骤、链接完整✅ 任务三：asr_report.md 三种方案对比、选型理由完整✅ 任务三：代码可运行，依赖清单完整✅ 任务三：experiment_log.md 实验记录完整✅ 目录结构符合要求
plaintext

---

## 五、`jianying.md`（独立剪映说明，可直接用）
```markdown
# 任务二：剪映AI音色克隆与配音产出说明

## 一、克隆步骤概要
1.  **准备素材**：打开剪映PC版，新建项目，导入一段参考视频作为底素材。
2.  **音色克隆**：
    - 点击「文本」→「新建文本」，输入测试文本；
    - 选中文本，点击「文本朗读」，选择「AI克隆」；
    - 录制1分钟本人清晰语音，完成音色克隆，保存为自定义音色。
3.  **配音生成**：
    - 导入DeepSeek大模型生成的文案，拆分为多段文本添加到时间轴；
    - 选中所有文本，选择克隆的自定义音色，自动生成配音。
4.  **导出存储**：预览无误后导出MP4视频，上传至夸克网盘。

## 二、导出文件格式
- 文件格式：MP4
- 编码：H.264视频 + AAC音频
- 分辨率：1080p (1920×1080)
- 帧率：30fps
- 音频参数：48kHz采样率，立体声

## 三、资源链接
- 视频文件：`lv_0_20260330204505.mp4`
- 夸克网盘链接：https://pan.quark.cn/s/0f976cb6ad42
- 提取方式：复制链接打开「夸克APP」即可获取
✅ 最后一步操作指南
下载模型：去 https://alphacephei.com/vosk/models 下载 vosk-model-small-cn-0.22，解压后改名为model，放进hw04文件夹
准备音频：把剪映导出的配音转成 16kHz 单声道 wav，放进assets文件夹
测试运行：先跑vosk_file.py，再跑vosk_realtime.py，确保无报错
