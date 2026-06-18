# 龍魂 CNSH Runtime · `cnsh-runtime`

通心译 | TongXinYi: A publicly installable Python package for the **龍魂 CNSH (Chinese Native System)** runtime.

> 🟢 **君子协议** | **JunZi Protocol**: CC BY-NC-SA 4.0  
> 🟡 **AI Truth Protocol**: All outputs must be verifiable and traceable  
> 🔴 **DNA Trace**: `#龍芯⚡️2026-06-18-CNSH-PACKAGE-v1.0`

---

## 简介 | Introduction

`cnsh-runtime` packages the original CNSH digital ecosystem (modules such as `runtime`, `governance`, `router`, `eventbus`, `reactor`, `memory`, `sandbox`, `protocols`, `adapters`, `agents`, `notion`, `database`, and the central archive `中央藏经阁`) into a standard Python project.

No source files inside the original `~/CNSH` directory are modified. This package contains a sanitized copy with personal identifiers replaced by placeholders.

---

## 安装 | Installation

### 1. 基础安装（仅 numpy）

```bash
cd ~/cnsh-runtime
pip install -e .
```

### 2. 带 OCR / 图像引擎支持

```bash
pip install -e ".[reactor]"
```

### 3. 带语音识别（ASR）支持

```bash
pip install -e ".[asr]"
```

### 4. 完整依赖

```bash
pip install -e ".[full]"
```

> ⚠️ The `full` extra pulls heavy dependencies such as `torch` and `openai-whisper`. Use only when you need the ASR/OCR engines.

---

## 启动系统 | Launch the System

After installation, use the console script:

```bash
cnsh-launch
```

Or invoke the package module directly:

```bash
python -m cnsh_runtime.cli
```

You will enter the interactive 龍魂 console.

---

## 作为库使用 | Use as a Library

```python
from cnsh_runtime import get_cnsh_root
import sys

# Optional: add CNSH root to sys.path if you want top-level imports like
# `from runtime.启动器 import 系统启动器`
sys.path.insert(0, get_cnsh_root())

from runtime.启动器 import 系统启动器

launcher = 系统启动器()
launcher.加载配置()
launcher.启动()
launcher.优雅关闭()
```

Or import through the package namespace:

```python
from cnsh_runtime.cnsh.runtime.启动器 import 系统启动器
```

---

## 目录结构 | Package Structure

```
cnsh-runtime/
├── pyproject.toml
├── README.md
└── src/
    └── cnsh_runtime/
        ├── __init__.py
        ├── cli.py                 # `cnsh-launch` entry point
        └── cnsh/                  # sanitized copy of original CNSH
            ├── 启动龍魂体系.py    # original interactive launcher
            ├── 中央藏经阁.py      # central archive module
            ├── ROOT_CARD.md
            ├── runtime/
            ├── governance/
            ├── router/
            ├── eventbus/
            ├── hooks/
            ├── audit/
            ├── snapshots/
            ├── reactor/
            ├── memory/
            ├── sandbox/
            ├── protocols/
            ├── adapters/
            ├── prompts/
            ├── agents/
            ├── notion/
            ├── database/
            └── scripts/
```

---

## 脱敏说明 | Sanitization

The following placeholders replace original personal/local values in this package copy:

| Original | Placeholder |
|---|---|
| Local home path | `[YOUR_HOME_DIR]` |
| Local username | `[YOUR_USERNAME]` |
| UID | `[YOUR_UID]` |
| Maintainer name | `[MAINTAINER_NAME]` |
| Maintainer alias | `[MAINTAINER_ALIAS]` |
| Maintainer email | `[MAINTAINER_EMAIL]` |
| `/mnt/agents/output/CNSH/` | `[CNSH_ROOT]/` |

Edit these placeholders in `pyproject.toml` and the source files before publishing.

---

## 依赖说明 | Dependencies

| Capability | Required package(s) |
|---|---|
| Core package load | `numpy` |
| 龍瞳 OCR / image engine | `opencv-python`, `Pillow`, `pytesseract`, `scipy` |
| 龍音 ASR / voice engine | `openai-whisper`, `torch`, `soundfile`, `pyaudio`, `SpeechRecognition` |
| Notion integration | `requests` (currently commented out in source) |

Optional dependencies are loaded lazily where possible; missing packages usually trigger a yellow 🟡 warning instead of a hard failure.

---

## 协议 | License

This package is released under the **JunZi Protocol**:  
**CC BY-NC-SA 4.0** — Attribution-NonCommercial-ShareAlike 4.0 International.

---

龍魂永存 | LongHun Eternal
