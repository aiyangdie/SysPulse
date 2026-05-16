@echo off
chcp 65001 >nul
title 硬件性能监控器
cd /d "%~dp0"
python main.py
pause