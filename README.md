# VidCutter

**Version:** 1.0.0  
**Date:** 2025-06-11  
**License:** MIT  

VidCutter is a fast and simple CLI tool that splits a video file into smaller parts based on your input duration in **minutes:seconds** format.

---

## 🔧 What It Does

1. Asks you for the full path of the video file.  
2. Asks for the part duration in `mm:ss` format.  
3. Splits the video into equal-length parts.  
4. Saves the parts inside a new folder named: [video name] parts (day_month_year hour_minute_second)

Each output file is named `[video name]_part_1.mp4`, `[video name]_part_2.mp4`, etc.

---

## ⚙️ Features

- Fast and lightweight  
- Simple and interactive  
- Output folder is timestamped to prevent overwrites  
- Ideal for content creators & social media editors  

---

## 📦 Requirements

- Python **3.12.9**  
- `moviepy` **1.0.3**  
> (The script may implicitly depend on `ffmpeg`, `ffmpeg-python`, `imageio`, and `imageio-ffmpeg`.  
> If you encounter errors, try installing these manually.)

Install requirements with:

```bash
pip install moviepy==1.0.3
```

## 🚀 Installation & Usage
Option 1: From Terminal
Open terminal or command prompt.

Navigate to the folder where VidCutter.py is located.

Run the script: