# 📺 YouTube Video Downloader

A powerful Python script powered by `yt-dlp` that enables you to download YouTube videos in high resolution with audio. Get detailed insights like format, resolution, and file size before downloading—all within a simple, user-friendly interface.

---

## ✨ Features
- 🎥 **High-Quality Downloads**: Get videos in MP4 format with the best available video and audio (up to 1440p or higher).
- 🔄 **Smart Retries**: Automatically retries up to 3 times on network failures.
- 🔍 **Preview Before Download**: See title, resolution, and file size, then confirm your download.
- 📁 **Organized Output**: Saves files neatly in a `downloads` folder.

---

## 📋 Prerequisites
- 🐍 **Python 3.x**: [Download here](https://www.python.org/downloads/).
- 🎵 **ffmpeg**: Essential for merging video and audio streams (installation guide below).

---

## 🚀 Setup Guide

### 1️⃣ Clone the Repository
```sh
git clone <repo-link>
cd <repo-folder>
```

### 2️⃣ Create a Virtual Environment (Recommended)
```sh
python -m venv venv
# Windows
venv\Scripts\activate  
# macOS/Linux
source venv/bin/activate  
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Install `ffmpeg`
1. Download the `ffmpeg` zip file.
2. Extract it and add the `bin` folder path to your system's environment variables.

To verify the installation, run:
```sh
ffmpeg --version
```

### 5️⃣ Run the Script
```sh
python script.py
```

### 6️⃣ Provide the Video URL
- The script will prompt you to enter a YouTube video URL.
- It will display details such as title, resolution, and file size.
- Confirm the download by typing `yes`.
- The download will start in the current directory under the downloads folder.

### 🎉 Boom! Downloading starts.

---

## 👥 Connect with Me
If you found this script helpful, follow me on:

- **[LinkedIn](#)** 👨‍💼
- **[GitHub](#)** 📚

Happy downloading! 🚀
