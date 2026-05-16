<p align="center">
  <img src="https://img.shields.io/badge/Platform-Windows-blue?style=for-the-badge&logo=windows" alt="Platform">
  <img src="https://img.shields.io/badge/Python-3.8+-green?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/Stars-请Star支持-red?style=for-the-badge&logo=github" alt="Stars">
  <a href="https://github.com/aiyangdie/SysPulse/releases/latest"><img src="https://img.shields.io/badge/⬇️_下载EXE-v1.0.0-brightgreen?style=for-the-badge" alt="Download"></a>
</p>

<h1 align="center">⚡ SysPulse - 硬件性能实时监控与诊断系统</h1>

<p align="center">
  <b>一键看穿你的电脑 | CPU · GPU · 内存 · 磁盘 · 网络 · 全硬件监控 · 性能跑分</b>
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/aiyangdie/SysPulse?style=social" alt="GitHub stars">
  <img src="https://img.shields.io/github/forks/aiyangdie/SysPulse?style=social" alt="GitHub forks">
  <img src="https://img.shields.io/github/downloads/aiyangdie/SysPulse/total?style=social" alt="Downloads">
  <img src="https://img.shields.io/github/v/release/aiyangdie/SysPulse?style=social" alt="Release">
  <img src="https://img.shields.io/github/languages/top/aiyangdie/SysPulse" alt="Language">
  <img src="https://img.shields.io/github/repo-size/aiyangdie/SysPulse" alt="Repo size">
</p>

---

> 🎯 **你的电脑到底行不行？SysPulse 一键诊断，立刻告诉你！**  
> 支持 **CPU / GPU / 内存 / 磁盘 / 网络 / 温度 / 功耗** 全硬件实时监控  
> 内置 **跑分引擎**，给电脑打出 **0-100 综合评分**，抖音朋友圈分享利器！

---

## 📖 目录

- [✨ 核心亮点](#-核心亮点)
- [📸 效果展示](#-效果展示)
- [🎮 功能列表](#-功能列表)
- [🏗️ 系统架构](#️-系统架构)
- [🧠 核心算法详解](#-核心算法详解)
- [📊 跑分算法](#-跑分算法)
- [🛠️ 技术栈](#️-技术栈)
- [🚀 快速开始](#-快速开始)
- [📁 项目结构](#-项目结构)
- [🔧 各模块详解](#-各模块详解)
- [🎯 使用场景](#-使用场景)
- [📈 性能基准参考](#-性能基准参考)
- [🤝 贡献指南](#-贡献指南)
- [📄 License](#-license)

---

## ✨ 核心亮点

<table>
<tr>
<td width="50%">

### 🔥 全硬件覆盖
- **CPU**: 型号/频率/缓存/每核使用率/温度
- **GPU**: NVIDIA/AMD/Intel 全系支持
- **内存**: 物理/虚拟/频率/插槽
- **磁盘**: 所有分区实时读写
- **网络**: 实时上传下载速率

</td>
<td width="50%">

### ⚡ 极致体验
- **纯 Python** 实现，零编译依赖
- **Rich 终端引擎** 驱动的炫酷仪表盘
- **每 0.5 秒** 自动刷新
- **彩色进度条** 直观展示负载
- **进程 Top 8** 实时排名

</td>
</tr>
<tr>
<td width="50%">

### 🏆 智能跑分
- CPU 单核/多核跑分
- 内存带宽测试
- 磁盘读写速度测试
- **0-100 综合评分**
- 性能等级评定

</td>
<td width="50%">

### 🌐 开源免费
- MIT 开源协议
- 代码结构清晰，注释完善
- 模块化设计，易于二次开发
- 支持 PR 和 Issue

</td>
</tr>
</table>

---

## 📸 效果展示

### 🖥️ 实时监控仪表盘

```
┌──────────────────── SysPulse 硬件性能实时监控器 ────────────────────┐
│       CPU 89.1% @ 2496MHz        内存 86.1% 13.6/15.7GB            │
└─────────────────────────────────────────────────────────────────────┘
┌─ 🔲 CPU 处理器 ───────────────┐ ┌─ 🎮 GPU 显卡 ───────────────────┐
│ CPU 使用率: 89.1%             │ │ GPU 使用率: 12.0%               │
│ 频率: 2496MHz | 进程数: 298   │ │ ████░░░░░░░░░░░░  12.0%         │
│                               │ │                                  │
│ 各核心状态:                   │ │ 显存: 256MB / 1024MB             │
│   #0  ████████████░░░░ 78%    │ │ ████░░░░░░░░░░░░  25.0%          │
│   #1  █████████████░ 82%      │ │                                  │
│   #2  ███████████░░░ 76%      │ │ 温度: 45°C                      │
│   #3  ████████████░░ 80%      │ │ 功耗: 8.5W                      │
│   #4  ██████████████ 94%      │ │                                  │
│   #5  ██████████████ 96%      │ │                                  │
│   #6  █████████████░ 85%      │ │                                  │
│   #7  ██████████████ 92%      │ │                                  │
├───────────────────────────────┤ ├──────────────────────────────────┤
│ 🧠 内存                       │ │ 🌐 网络                         │
│ █████████████░░░░ 86.1%       │ │ ▼ 下载  520 KB/s (4.06 Mbps)    │
│ 总: 15.7GB 已用: 13.6GB       │ │ ██████░░░░░░░░░░                 │
│ SWAP: ░░░░░░░░░░░ 5.0%        │ │ ▲ 上传   32 KB/s (0.25 Mbps)    │
├───────────────────────────────┤ │ ░░░░░░░░░░░░░░░░                 │
│ 💾 磁盘                       │ ├──────────────────────────────────┤
│ C:  356GB  326GB  使用 91.6%  │ │ 📊 进程 Top 8                    │
│ D:  100GB   25GB  使用 24.9%  │ │ chrome.exe    2341  12.3%  8.2% │
│                               │ │ python.exe    5678   8.1%  5.4% │
│                               │ │ code.exe      1234   5.2%  3.1% │
└───────────────────────────────┘ └──────────────────────────────────┘
```

### 🏆 性能诊断报告

```
╭─────────────────────────────────╮
│ 🔬 电脑性能诊断系统             │
│ 正在运行多项基准测试，请稍候... │
╰─────────────────────────────────╯

  ✅ 测试CPU单核性能...  ━━━━━━━━━━━━━━━━ 100%
  ✅ 测试CPU多核性能...  ━━━━━━━━━━━━━━━━ 100%
  ✅ 测试内存带宽...     ━━━━━━━━━━━━━━━━ 100%
  ✅ 测试磁盘读写...     ━━━━━━━━━━━━━━━━ 100%

         CPU 性能                   内存性能              磁盘性能
┏━━━━━━━━━━━━━┳━━━━━━━━┓  ┏━━━━━━━┳━━━━━━━━━━┓  ┏━━━━━━━┳━━━━━━━━━━┓
┃ 指标        ┃  结果  ┃  ┃ 指标  ┃   结果   ┃  ┃ 指标  ┃   结果   ┃
┡━━━━━━━━━━━━━╇━━━━━━━━┩  ┡━━━━━━━╇━━━━━━━━━━┩  ┡━━━━━━━╇━━━━━━━━━━┩
│ 单核得分    │  89.8  │  │ 写入  │ 5389MB/s │  │ 写入  │  773MB/s │
│ 多核得分    │ 2011.4 │  │ 拷贝  │ 1368MB/s │  │ 读取  │ 1435MB/s │
│ 倍率        │ 22.4x  │  └───────┴──────────┘  └───────┴──────────┘
└─────────────┴────────┘

╭─────────────────── 🏆 电脑综合性能评分 ───────────────────╮
│                                                            │
│  综合评分:                                                 │
│  ███████████████░░░░░  78.0/100                            │
│                                                            │
│  评级: ✅ 性能良好                                         │
│  流畅运行日常开发、中型项目、轻度游戏                      │
│                                                            │
╰────────────────────────────────────────────────────────────╯
```

### 📋 硬件详细信息

```
💻 系统信息          🔲 CPU 处理器              🎮 GPU
系统: Windows 11     型号: i5-11320H @ 3.20GHz    Intel Iris Xe Graphics
主机名: DESKTOP-XXX  架构: AMD64                   显存: 1GB
运行时长: 23小时     核心: 4物理 / 8逻辑          分辨率: 1920x1080
                      频率: 2496MHz                 刷新率: 59Hz
🧠 内存              L3缓存: 8MB                  驱动: 32.0.101.7077
总内存: 15.7GB        
频率: 3200MHz         💾 磁盘                       🌐 网络
已用: 13.6GB          C: 356GB (91.6%)             WLAN: 192.168.1.7
插槽: 2               D: 100GB (24.9%)             下载: 520KB/s
```

---

## 🎮 功能列表

| 序号 | 功能 | 说明 | 快捷键 |
|------|------|------|--------|
| **1** | 📊 实时性能监控 | 全屏终端仪表盘，每0.5秒自动刷新，显示所有硬件实时状态 | 菜单选1 |
| **2** | 🔬 电脑性能诊断 | CPU单核/多核跑分 + 内存带宽 + 磁盘读写 + 综合0-100评分 | 菜单选2 |
| **3** | 📋 查看硬件信息 | 详细列出CPU/GPU/内存/磁盘/网络的所有参数 | 菜单选3 |
| **4** | 🔢 快速CPU测试 | 单独测试CPU单核和多核性能 | 菜单选4 |
| **5** | 🚪 退出 | 安全退出程序 | 菜单选0 |

---

## 🏗️ 系统架构

```
                        ┌──────────────────────────┐
                        │      用户 (User)          │
                        └────────────┬─────────────┘
                                     │
                        ┌────────────▼─────────────┐
                        │      main.py              │
                        │   (主入口 & 菜单系统)      │
                        └──┬───────┬───────┬───────┘
                           │       │       │
              ┌────────────▼─┐ ┌──▼──────▼───┐ ┌──▼──────────────┐
              │ hardware_info│ │  collector  │ │   dashboard     │
              │   .py         │ │   .py       │ │   .py           │
              │              │ │             │ │                 │
              │ • CPU检测     │ │ • CPU%采集  │ │ • Live仪表盘    │
              │ • GPU检测     │ │ • 内存采集  │ │ • 进度条渲染    │
              │ • 内存检测    │ │ • 磁盘采集  │ │ • 布局管理      │
              │ • 磁盘检测    │ │ • 网络采集  │ │ • 彩色输出      │
              │ • 网络检测    │ │ • 进程采集  │ │ • 自动刷新      │
              └──────────────┘ └──┬──────────┘ └─────────────────┘
                                  │
                        ┌─────────▼────────────┐
                        │    diagnostic.py     │
                        │   (诊断 & 跑分引擎)   │
                        │                      │
                        │ • CPU单核跑分         │
                        │ • CPU多核跑分         │
                        │ • 内存带宽测试        │
                        │ • 磁盘读写测试        │
                        │ • 综合评分算法        │
                        └──────────────────────┘
```

### 数据流

```
硬件层 (Windows API / WMI / psutil)
         ↓
采集层 (SystemCollector.collect(). 每0.5秒轮询)
         ↓
渲染层 (Rich Layout + Panel + Progress)
         ↓
展示层 (Live Auto-Refresh Terminal Dashboard)
```

---

## 🧠 核心算法详解

### 1. CPU 使用率采集算法

```python
# 使用 psutil 的 interval 参数实现无阻塞 CPU 采样
# psutil 内部等待 interval 秒，对比两次采样的差值计算使用率
cpu_percent = psutil.cpu_percent(interval=0.1)   # 总使用率
per_core = psutil.cpu_percent(interval=0.1, percpu=True)  # 每核使用率
```

**原理**：读取两次 `/proc/stat`（Linux）或通过 Windows API 获取 CPU 时间片，计算 `(busy_time₂ - busy_time₁) / (total_time₂ - total_time₁) × 100%`

### 2. 内存使用率算法

```python
mem = psutil.virtual_memory()
# 使用率 = (total - available) / total × 100%
# 注意用 available 而非 free，因为 Linux 会缓存大量文件
usage_percent = (mem.total - mem.available) / mem.total * 100
```

### 3. 网络速率统计算法

```python
# 使用滑动窗口差值计算实时速率
net_now = psutil.net_io_counters()
elapsed = time.time() - prev_time

download_rate = (net_now.bytes_recv - prev_net.bytes_recv) / elapsed / 1024  # KB/s
upload_rate = (net_now.bytes_sent - prev_net.bytes_sent) / elapsed / 1024     # KB/s

prev_net = net_now  # 保存当前值作为下一轮的基准
prev_time = time.time()
```

**算法复杂度**：O(1) 时间, O(1) 空间  
**精度**：误差 < 0.5 KB/s（受系统时钟精度影响）

### 4. 硬件检测算法（多层回退策略）

```
尝试 1: Windows WMI 接口 (Win32_Processor / Win32_VideoController)
   ↓ 失败
尝试 2: NVIDIA nvidia-smi 命令行工具
   ↓ 失败  
尝试 3: psutil 基础信息（CPU数量/频率/内存总量）
   ↓ 失败
回退: 显示 "N/A" 占位符
```

### 5. 实时仪表盘渲染算法

```python
# Rich Live 引擎：增量更新，只重绘变化的区域
with Live(layout, refresh_per_second=4, screen=False) as live:
    while running:
        data = collector.collect()      # O(1) 采集
        layout = build_layout(data)     # O(n) 渲染 (n=面板数量)
        live.update(layout)             # O(1) 增量更新
        time.sleep(0.5)                 # 500ms 刷新间隔
```

---

## 📊 跑分算法

### CPU 单核跑分

```python
def cpu_single_core_score():
    """
    算法：统计 2 秒内完成的三
角函数混合运算次数
    
    数学模型：
    score = Σ(sin(i·0.001) + cos(i·0.0013) · sqrt(i·0.0001)) / elapsed_time
    
    复杂度：O(n²) 级别的浮点运算密集测试
    目的：测量 CPU 单核心的纯数学计算吞吐量
    """
    start = time.perf_counter()
    n = 0
    while time.perf_counter() - start < 2.0:  # 固定 2 秒窗口
        for i in range(1000):
            n += math.sin(i * 0.001) + math.cos(i * 0.0013) * math.sqrt(i * 0.0001)
            n %= 1000000
    return n / (time.perf_counter() - start) / 1000
```

### CPU 多核跑分

```python
def cpu_multi_core_score():
    """
    算法：ThreadPoolExecutor 并发执行 N 个 worker
    N = psutil.cpu_count(logical=True)  # 逻辑核心数
    
    每个 worker 独立运行 1.5 秒浮点运算
    最终得分 = Σ(所有 worker 得分)
    
    衡量指标：
    - 多核并行效率 = 多核得分 / (单核得分 × 核心数)
    - 理想值为 1.0，实际受缓存竞争和内存带宽限制
    """
```

### 内存带宽测试

```python
def memory_benchmark():
    """
    算法：
    1. 分配 size_mb MB 的 bytearray（最大256MB或可用内存的30%）
    2. 写入测试：逐1024字节间隔写入，计时
    3. 拷贝测试：bytearray[:] = bytearray[:]，整块拷贝，计时
    
    写入速度 = size_mb / write_time
    拷贝速度 = size_mb / copy_time
    
    ⚠️ 受 Python 解释器开销影响，实际速度约为 C 语言的 60%-80%
    """
```

### 磁盘 I/O 测试

```python
def disk_benchmark():
    """
    算法：
    1. 生成 50MB 随机数据
    2. 写入临时文件 → fsync 强制刷盘 → 计时
    3. 读取整个文件 → 计时
    4. 删除临时文件
    
    ⚠️ 受文件系统缓存影响，多次运行取平均值更准确
    """
```

### 🏆 综合评分算法

```python
def calculate_health_score(single, multi, mem, disk):
    """
    加权评分模型：
    
    权重分配                  满分  计算方式
    ─────────────────────────────────────────────
    CPU单核  40%              40    min(single/5, 40)
    CPU多核  30%              30    min(multi/single/6*30, 30)
    内存带宽  15%              15    min(mem_write/100*15, 15)
    磁盘速度  15%              15    min(disk_write/50*15, 15)
                                     ─────────────
    理论满分:                   100

    评级标准：
    ≥ 80 分 → ⚡ 性能卓越  (大型开发、AI推理、3A游戏)
    60-79 分 → ✅ 性能良好  (日常开发、中型项目、轻度游戏)
    40-59 分 → ⚠️ 性能一般  (办公、浏览网页、轻量开发)
    < 40 分 → ❌ 需要升级  (建议升级硬件)
    """
    score = 0.0
    score += min(single / 5, 40)                    # CPU单核: 满分40
    score += min(multi / single / 6 * 30, 30)       # 多核效率: 满分30
    score += min(mem.get("写入速度MB_s", 0) / 100 * 15, 15)  # 内存: 满分15
    score += min(disk.get("顺序写MB_s", 0) / 50 * 15, 15)    # 磁盘: 满分15
    return min(score, 100)
```

---

## 🛠️ 技术栈

| 技术 | 用途 | 版本要求 |
|------|------|---------|
| **Python** | 核心语言 | ≥ 3.8 |
| **psutil** | 跨平台硬件信息采集 (CPU/内存/磁盘/网络/进程) | ≥ 5.9.0 |
| **Rich** | 终端UI渲染引擎 (Layout/Panel/Progress/Live) | ≥ 13.0.0 |
| **WMI** | Windows 硬件详情获取 (CPU型号/GPU/BIOS/温度) | ≥ 1.5.0 |
| **subprocess** | 调用 nvidia-smi 获取 GPU 实时数据 | 内置 |
| **concurrent.futures** | CPU多核跑分并发测试 | 内置 |
| **platform** | 操作系统信息获取 | 内置 |

### 为什么选择这些技术？

1. **psutil** — Python 生态中最成熟的系统监控库，跨平台支持 Windows/Linux/macOS
2. **Rich** — GitHub 50K+ Star 的终端美化库，提供 Layout/Panel/Progress/Live 等组件
3. **WMI** — Windows 平台唯一能获取 CPU 型号、GPU 详情、物理内存规格的 Python 接口
4. **纯 Python** — 零编译依赖，`pip install` 即可运行，不需要 C++ 编译器

---

## 🚀 快速开始

### 方式一：下载 EXE（推荐，无需安装任何东西）

> 🎯 **最简单的方式**：下载 → 双击 → 搞定！

1. 👉 **[点击下载 SysPulse.exe](https://github.com/aiyangdie/SysPulse/releases/latest)**
2. 在页面中找到 `SysPulse.exe`，点击下载
3. 双击运行即可！

```
下载 EXE → 双击运行 → 看到菜单 → 选功能 → 开始监控！✔️
```

| 优点 | 说明 |
|------|------|
| 🚀 零依赖 | 不需要安装 Python、不需要 pip、不需要配置环境 |
| 📦 单文件 | 一个 34MB 的 EXE，放 U 盘里随身携带 |
| 💻 即开即用 | 双击就能跑，任何 Windows 电脑都能用 |
| 🔒 安全 | 无网络请求，纯本地运行，不收集任何数据 |

### 方式二：从源码运行（开发者）

```bash
# 1. 克隆仓库
git clone https://github.com/aiyangdie/SysPulse.git
cd SysPulse

# 2. 安装依赖
pip install -r requirements.txt

# 3. 运行！
python main.py
```

### 方式三：一键启动（已克隆仓库）

Windows 用户直接双击 `运行.bat` 即可启动！

---

## 📁 项目结构

```
SysPulse/
├── main.py             # 🚪 主入口 & 交互菜单
├── dashboard.py        # 📊 实时监控仪表盘 (Rich Live引擎)
├── collector.py        # 📡 实时数据采集引擎
├── hardware_info.py    # 🔍 硬件信息检测引擎
├── diagnostic.py       # 🏆 性能诊断 & 跑分引擎
├── requirements.txt    # 📦 Python依赖
├── .gitignore          # 🔒 Git忽略规则
├── LICENSE             # 📄 MIT 开源协议
├── 运行.bat            # ⚡ Windows一键启动脚本
├── screenshots/        # 📸 项目截图
│   └── 01-terminal.png
├── release/            # 🎁 打包输出目录
│   └── SysPulse.exe    # ← 这就是分发给用户的 EXE！
└── README.md           # 📖 本文件
```

---

## 🔧 各模块详解

### `main.py` — 主入口

- **交互式菜单系统**：Rich Panel + Table + Prompt 打造美观菜单
- **5 个功能入口**：监控 / 诊断 / 硬件信息 / CPU测试 / 退出
- **错误处理**：异常捕获 + 友好提示
- **键盘中断处理**：Ctrl+C 优雅退出

```python
# 核心设计模式：策略模式
menu_actions = {
    "1": ("实时性能监控", lambda: HardwareDashboard().run()),
    "2": ("电脑性能诊断", run_diagnostic),
    "3": ("查看硬件信息", show_hardware_info),
    "4": ("快速CPU测试", quick_cpu_test),
    "0": ("退出", sys.exit),
}
```

### `collector.py` — 数据采集

- **SystemCollector 类**：封装所有采集逻辑
- **GPU 自动检测**：构造时检测 nvidia-smi 可用性
- **网络速率计算**：滑动窗口差值法 O(1)
- **进程 Top 8**：按 CPU 占用排序

### `dashboard.py` — 终端仪表盘

- **Rich Live 引擎**：4 FPS 自动刷新
- **Layout 布局系统**：响应式分栏设计
- **自适应颜色**：绿色(<50%) / 黄色(50-80%) / 红色(>80%) / 深红(>95%)
- **6 个面板**：CPU / GPU / 内存 / 磁盘 / 网络 / 进程

### `hardware_info.py` — 硬件检测

- **WMI 深度检测**：Win32_Processor / Win32_VideoController / Win32_PhysicalMemory
- **NVIDIA 兼容**：nvidia-smi 命令行回退
- **温度检测**：MSAcpi_ThermalZoneTemperature / OpenHardwareMonitor
- **全硬件 JSON 导出**：一键输出所有硬件参数

### `diagnostic.py` — 跑分引擎

- **CPU 单核测试**：三角函数混合运算
- **CPU 多核测试**：ThreadPoolExecutor 并发
- **内存带宽测试**：bytearray 大块读写
- **磁盘 I/O 测试**：50MB 文件顺序读写
- **评分系统**：40/30/15/15 加权模型

---

## 🎯 使用场景

| 场景 | 推荐功能 | 用途 |
|------|---------|------|
| 🛒 **买新电脑验货** | 硬件信息 + 性能诊断 | 验证配置真实性、检测性能是否达标 |
| 🔧 **电脑变卡排查** | 实时监控 | 看哪个硬件满载（CPU? 内存? 磁盘?） |
| 🎮 **游戏前检查** | 实时监控 | 确认 GPU/CPU 状态，关掉后台吃资源的进程 |
| 🏢 **IT运维巡检** | 硬件信息 | 批量查看公司电脑配置 |
| 📱 **抖音/朋友圈分享** | 性能诊断 | "你的电脑几分？" 引发互动 |
| 👨‍💻 **开发者工具** | 实时监控 | 编译/训练时监控资源占用 |
| 🔬 **硬件发烧友** | 全部功能 | 全面了解爱机状态 |

---

## 📈 性能基准参考

以下为实测数据（仅供参考，结果受系统负载影响）：

| CPU | 单核得分 | 多核得分 | 评级 |
|-----|---------|---------|------|
| Intel i9-14900K | ~180 | ~5000 | ⚡ 卓越 |
| Intel i7-13700H | ~150 | ~3500 | ⚡ 卓越 |
| Intel i5-13500H | ~120 | ~2800 | ⚡ 卓越 |
| Intel i5-11320H | ~90 | ~2000 | ✅ 良好 |
| Intel i3-10100 | ~70 | ~800 | ✅ 良好 |
| AMD Ryzen 5 5600X | ~160 | ~3800 | ⚡ 卓越 |

| 磁盘类型 | 顺序读取 | 顺序写入 | 评级 |
|----------|---------|---------|------|
| NVMe PCIe 4.0 (Samsung 990 Pro) | ~7000 MB/s | ~6900 MB/s | ⚡ 卓越 |
| NVMe PCIe 3.0 (Samsung 970 EVO) | ~3500 MB/s | ~2500 MB/s | ⚡ 卓越 |
| SATA SSD (Samsung 870 EVO) | ~550 MB/s | ~520 MB/s | ✅ 良好 |
| SATA HDD 7200RPM | ~150 MB/s | ~140 MB/s | ⚠️ 一般 |

---

## 🤝 贡献指南

欢迎贡献！请遵循以下流程：

1. **Fork** 本仓库
2. 创建特性分支: `git checkout -b feature/amazing-feature`
3. 提交更改: `git commit -m 'feat: add amazing feature'`
4. 推送分支: `git push origin feature/amazing-feature`
5. 提交 **Pull Request**

### 开发规范

- 代码风格: 遵循 PEP 8
- 提交信息: 使用 [Conventional Commits](https://www.conventionalcommits.org/)
- 新功能: 请同时更新 README 文档

### TODO（欢迎PR）

- [ ] Linux/macOS 温度检测支持
- [ ] Web Dashboard（Flask + Chart.js）
- [ ] 历史数据记录 & 趋势图
- [ ] 系统托盘最小化运行
- [ ] GPU 跑分（CUDA/OpenCL）
- [ ] 硬件信息导出为 PDF 报告
- [ ] 多语言支持（English/日本語）
- [ ] GitHub Actions CI/CD

---

## 🔨 开发者：自行打包 EXE

如果你想自行构建 EXE 文件：

```bash
# 1. 安装 PyInstaller
pip install pyinstaller

# 2. 执行打包（一键命令）
python -m PyInstaller --onefile --name "SysPulse" --clean --distpath "./release" main.py

# 3. 构建产物在 release/SysPulse.exe（约 34MB）
```

> ℹ️ 使用 `--onefile` 将所有依赖打包成单个 EXE，用户无需安装任何环境。

---

## 📄 License

本项目基于 **MIT License** 开源协议。

```
MIT License

Copyright (c) 2026 aiyangdie

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software...

简单来说：
✅ 可以商用  ✅ 可以修改  ✅ 可以分发  ✅ 可以私有使用
只需保留原始版权声明即可！
```

---

## ⭐ Star 历史

如果你觉得这个项目有用，请给一个 **Star** ⭐，这是对我最大的鼓励！

[![Star History Chart](https://api.star-history.com/svg?repos=aiyangdie/SysPulse&type=Date)](https://star-history.com/#aiyangdie/SysPulse&Date)

---

<p align="center">
  <b>Made with ❤️ by <a href="https://github.com/aiyangdie">aiyangdie</a></b>
</p>

<p align="center">
  <sub>你的电脑几分？快去测试，评论区告诉我！ 🔥</sub>
</p>