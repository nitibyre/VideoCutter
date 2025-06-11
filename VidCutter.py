import os
from moviepy.video.io.VideoFileClip import VideoFileClip
from datetime import datetime

def convert_to_seconds(time_str):
    try:
        parts = time_str.split(':')
        if len(parts) != 2:
            return None
        minutes = int(parts[0])
        seconds = int(parts[1])
        if minutes < 0 or seconds < 0 or seconds >= 60:
            return None
        return minutes * 60 + seconds
    except:
        return None

while True:
    video_path = input("Enter the full path and name of the video file (e.g., C:\\Users\\AAAaa\\Desktop\\New folder\\video.mp4): ").strip()
    if os.path.isfile(video_path):
        break
    else:
        print("The file you entered was not found. Please enter the correct and full path.")

while True:
    time_input = input("Enter the part length in mm:ss format (e.g., 02:30 for 2 minutes 30 seconds): ").strip()
    clip_duration = convert_to_seconds(time_input)
    if clip_duration is None or clip_duration <= 0:
        print("Please enter a valid time in mm:ss format, with seconds less than 60.")
        continue
    break

clip = VideoFileClip(video_path)
video_length = clip.duration

video_name = os.path.splitext(os.path.basename(video_path))[0]

now = datetime.now()
timestamp = now.strftime("%d_%m_%Y %H_%M_%S")

folder_name = f"{video_name} parts ({timestamp})"

if not os.path.exists(folder_name):
    os.makedirs(folder_name)

number_of_parts = int(video_length // clip_duration)
if video_length % clip_duration != 0:
    number_of_parts += 1

print(f"The video is {video_length:.2f} seconds long and will be saved in {number_of_parts} parts.\n")

for i in range(number_of_parts):
    start = i * clip_duration
    end = min((i + 1) * clip_duration, video_length)
    part = clip.subclip(start, end)

    file_name = os.path.join(folder_name, f"{video_name}_parts_{i+1}.mp4")
    print(f"Saving {file_name}... ({start:.2f}-{end:.2f} seconds)")
    part.write_videofile(file_name, codec="libx264")

clip.close()
print("All parts have been successfully saved!")
