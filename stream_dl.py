"""
This script will record a livestream video such as youtube or twitch which is usually unable to download by normal tools
"""
import urllib
import m3u8
import streamlink
import time
import argparse
import random
from datetime import timedelta


def get_stream(url):
    """
    Get upload chunk url
    """
    streams = streamlink.streams(url)
    stream_url = streams["best"]

    m3u8_obj = m3u8.load(stream_url.args['url'])

    return m3u8_obj.segments


def dl_stream(args):
    """
    Download chunks and turn them to multiple small clips
    """
    # Set arguments
    filename = 'live'
    directory = args.output_dir
    if directory != '':
        directory += '/'
    chunks = args.chunks    
    count = chunks + 1
    pre_time_stamp = 0

    # Run forever or a number of times
    while count>0 or chunks == -1:
        count = count-1

        # Initialize variables
        stream_segments = get_stream(args.url)
        num_of_segments = len(stream_segments)
        cur_time_stamp = stream_segments[0].current_program_date_time.strftime("%Y%m%d-%H%M%S")

        # This is to reduce the frequency of recording the same chunk
        if pre_time_stamp == cur_time_stamp:
            time_sleep = random.random()
            print(f"Sleep for {time_sleep} s.")
            time.sleep(time_sleep)
        else:
            # Write files
            for i in range(num_of_segments):
                time_stamp = stream_segments[i].current_program_date_time.strftime("%Y%m%d-%H%M%S")
                print(f'Downloading {time_stamp}')
                file = open(directory + filename + '_' + str(time_stamp) + '.ts', 'wb+')
                with urllib.request.urlopen(stream_segments[i].uri) as response:
                    html = response.read()
                    file.write(html)
            
            # Update previous time stamp
            pre_time_stamp = cur_time_stamp


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--url",
        type=str,
        default='',
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        default='',
    )
    # parser.add_argument(
    #     "-name",
    #     type=str,
    #     default='live'
    # )
    parser.add_argument(
        "--chunks",
        type=int,
        default=-1
    )
    args = parser.parse_args()

    dl_stream(args)


if __name__ == '__main__':
    main()