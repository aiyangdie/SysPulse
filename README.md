<p align="center">
  <img src="https://img.shields.io/badge/Platform-Windows-blue?style=for-the-badge&logo=windows" alt="Platform">
  <img src="https://img.shields.io/badge/Python-3.8+-green?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License">
</p>

<h1 align="center">⚡ SysPulse</h1>

<p align="center">
  <b>硬件性能实时监控与诊断系统</b>
</p>

<p align="center">
  CPU · GPU · 内存 · 磁盘 · 网络 · 全硬件实时监控 · 性能跑分 · 综合评分
</p>

---

## 📌 项目简介

SysPulse 是一款基于 Python 的终端硬件监控与诊断工具，通过 Rich 引擎驱动的炫酷仪表盘，实现对 CPU、GPU、内存、磁盘、网络等全硬件的实时监控。内置跑分引擎，可为电脑打出 0-100 综合性能评分，快速评估硬件状态。

> 🎯 你的电脑到底行不行？SysPulse 一键诊断，立刻告诉你！

---

## ✨ 核心特性

- 📊 **实时性能监控** — 全屏终端仪表盘，每 0.5 秒自动刷新，6 大面板同时展示
- 🔬 **电脑性能诊断** — CPU 单核/多核跑分 + 内存带宽 + 磁盘读写 + 0-100 综合评分
- 📋 **硬件信息检测** — 详细列出 CPU/GPU/内存/磁盘/网络的所有参数
- 🔢 **快速 CPU 测试** — 单独测试 CPU 单核和多核性能
- 🎨 **自适应颜色** — 绿色(<50%) / 黄色(50-80%) / 红色(>80%) / 深红(>95%) 直观展示负载
- 🏆 **智能评分** — 加权评分模型（CPU 40% + 多核效率 30% + 内存 15% + 磁盘 15%）
- 🖥️ **NVIDIA GPU 支持** — 自动检测 nvidia-smi，实时显示 GPU 使用率/显存/温度/功耗
- 🔄 **多层回退检测** — WMI → nvidia-smi → psutil，确保最大兼容性

---

## 🛠️ 技术栈

| 技术 | 用途 | 版本 |
|------|------|------|
| **Python** | 核心语言 | ≥ 3.8 |
| **psutil** | 跨平台硬件信息采集 | ≥ 5.9.0 |
| **Rich** | 终端 UI 渲染引擎 (Layout/Panel/Progress/Live) | ≥ 13.0.0 |
| **WMI** | Windows 硬件详情获取 | ≥ 1.5.0 |
| **concurrent.futures** | CPU 多核跑分并发测试 | 内置 |

---

## 🚀 快速开始

### 前置条件

- Python 3.8+
- Windows 操作系统（WMI 依赖）
- NVIDIA GPU（可选，用于 GPU 监控）

### 安装步骤

```bash
git clone https://github.com/aiyangdie/SysPulse.git
cd SysPulse
pip install -r requirements.txt
```

### 运行命令

```bash
python main.py
```

Windows 用户也可直接双击 `运行.bat` 一键启动。

---

## 📂 项目结构

```
SysPulse/
├── main.py             # 主入口 & 交互菜单
├── dashboard.py        # 实时监控仪表盘 (Rich Live 引擎)
├── collector.py        # 实时数据采集引擎
├── hardware_info.py    # 硬件信息检测引擎
├── diagnostic.py       # 性能诊断 & 跑分引擎
├── requirements.txt    # Python 依赖
├── 运行.bat            # Windows 一键启动脚本
├── screenshots/        # 项目截图
│   └── 01-terminal.png
├── LICENSE             # MIT 开源协议
└── README.md
```

---

## 🤝 贡献与许可证

欢迎贡献！请遵循以下流程：

1. **Fork** 本仓库
2. 创建特性分支: `git checkout -b feature/amazing-feature`
3. 提交更改: `git commit -m 'feat: add amazing feature'`
4. 推送分支: `git push origin feature/amazing-feature`
5. 提交 **Pull Request**

本项目基于 **MIT License** 开源协议。详见 [LICENSE](LICENSE)。
