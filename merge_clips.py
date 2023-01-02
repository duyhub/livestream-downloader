import os
import subprocess


# filename list in the directory
dir_list = os.listdir()

# Get filename with extention ".ts"
videoname_list = [name for name in dir_list if name[-3:] == '.ts'and name[:4] == 'live'] # and (name[-4] == '5' or name[-4] == '0')]
videoname_list = sorted(videoname_list)
print(videoname_list[-10:])
print(len(videoname_list))

# Prepare text file for ffmpeg to concat videos
with open('video_list.txt','w') as file:
    for name in videoname_list:
        file.write(f"file '{name}'\n")


output_filename = 'final_clip'
subprocess.call(f'ffmpeg -y -f concat -safe 0 -i video_list.txt -c copy {output_filename}.ts', shell=True)