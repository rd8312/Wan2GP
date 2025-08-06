# FFmpeg 下载问题解决方案

## 问题描述
在运行 `wgp.py` 时，可能会遇到网络下载错误，导致程序崩溃。这通常发生在下载 FFmpeg 时网络连接不稳定或中断。

## 错误信息示例
```
requests.exceptions.ChunkedEncodingError: ('Connection broken: IncompleteRead (10485760 bytes read, 81748588 more expected)', IncompleteRead (10485760 bytes read, 81748588 more expected))
```

## 解决方案

### 方案 1: 使用改进的下载功能（推荐）
程序已经更新了 `download_ffmpeg()` 函数，现在包含：
- 重试机制（最多3次）
- 网络连接检查
- 更好的错误处理
- 自动清理不完整文件

### 方案 2: 跳过 FFmpeg 下载
如果网络问题持续存在，可以跳过 FFmpeg 下载：

#### Windows 批处理文件
运行 `run_without_ffmpeg.bat` 文件

#### PowerShell 脚本
运行 `run_without_ffmpeg.ps1` 文件

#### 手动设置环境变量
在命令行中执行：
```cmd
set SKIP_FFMPEG_DOWNLOAD=true
python wgp.py
```

或在 PowerShell 中执行：
```powershell
$env:SKIP_FFMPEG_DOWNLOAD = "true"
python wgp.py
```

### 方案 3: 手动下载 FFmpeg
1. 访问 https://github.com/GyanD/codexffmpeg/releases
2. 下载最新的 `essentials_build.zip`
3. 解压并将 `ffmpeg.exe`、`ffprobe.exe`、`ffplay.exe` 放到程序目录

## 注意事项
- 跳过 FFmpeg 下载后，某些视频处理功能可能不可用
- 建议在网络稳定时重新尝试下载
- 如果问题持续存在，请检查防火墙或代理设置 