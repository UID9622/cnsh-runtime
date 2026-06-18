#龍芯⚡️2026-06-18-CNSH-PACKAGE-v1.0
"""
通心译 | TongXinYi: CNSH Runtime Package
龍魂体系·中文原生数字生态 — 公开可安装Python包

CNSH (Chinese Native System / 龍魂) runtime packaged for `pip install`.
All original CNSH modules live under `cnsh_runtime.cnsh`.
"""
# 🟢 君子协议 | JunZi Protocol: CC BY-NC-SA 4.0
# 🟡 AI Truth Protocol: All outputs must be verifiable and traceable
# 🔴 DNA Trace: #龍芯⚡️2026-06-18-CNSH-PACKAGE-v1.0

__version__ = "2026.6.18"
__dna__ = "#龍芯⚡️2026-06-18-CNSH-PACKAGE-v1.0"


def get_cnsh_root() -> str:
    """Return the absolute path to the bundled CNSH root directory."""
    import os
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "cnsh")
