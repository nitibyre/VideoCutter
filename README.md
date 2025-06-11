# Video Splitter

This Python script splits a video file into smaller parts of a specified length.  
The part length is entered in **mm:ss** (minutes:seconds) format.  

## Features

- Takes full path of the video file as input.  
- Takes part length in mm:ss format (e.g. 02:30 for 2 minutes 30 seconds).  
- Automatically creates a folder named as `videoName parts (dd_mm_yyyy hh_mm_ss)` to store the output parts.  
- Saves the video parts as `part_1.mp4`, `part_2.mp4`, etc. inside the folder.  
- Supports any video length and splits accordingly.  

## Requirements

- Python 3.x  
- moviepy (`pip install moviepy`)  

## How to Use

1. Open your terminal or command prompt.  
2. Run the script by typing:  
   ```bash
   python video_splitter.py
When prompted, enter the full path to your video file.

Enter the part length in mm:ss format (e.g., 05:00 for 5 minutes).

The script will create a timestamped folder and save the split video parts inside it.

Wait until the script finishes processing.

Notes
Ensure the video file path is correct and accessible.

The script validates the mm:ss format and seconds must be less than 60.

Output folder includes a timestamp to avoid overwriting existing folders.

License
This project is licensed under the MIT License.

Created with ❤️ by [Your Name]