# Livestream downloading script using Python
This script can record a livestream session on Youtube or Twitch while normal downloading tools can't download since it's a live event.

## Prerequisites

On your local development machine, install the following tools:
- git
- python3
- pip

1. Clone the GitHub repository

        git clone https://github.com/duyhub/livestream-downloader

2. Create a new python3 virtual environment:

        python3 -m venv venv

3. Activate the virtual environment:

        source venv/bin/activate

4.  Install the required Python modules:

        pip3 install -r requirements.txt

## Run the script

        python3 stream_dl.py --url <livestream link>
    
Example: python3 stream_dl.py --url https://www.youtube.com/watch?v=abcxyz 

To stop recording, press Ctrl+C or Command+C to terminate

The script will generate many small clips from the recording session. Next step is to concatenate all small clips into one video.

## Merge into one video

### Requirement

Your local machine needs to install `ffmpeg` to run this script.

### Merge small clips

Run merge_clips.py

        python3 merge_clips.py