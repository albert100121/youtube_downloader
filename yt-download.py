"""
youtube_dl package and usage
https://github.com/ytdl-org/youtube-dl

How to run
python yt-download.py --url [URL]
or
python yt-download.py --urls_txt [xxx.txt]


"""
import os
import argparse
from xml.dom import NotFoundErr
import youtube_dl
from typing import List


def get_args():
    """Get the arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-u",
        "--url",
        type=str,
        help="The url for youtube video",
    )
    parser.add_argument(
        "-t",
        "--urls_txt",
        type=str,
        help="The url",
    )
    parser.add_argument(
        "-o",
        "--output_dir",
        type=str,
        help="The path for output videos to be stored",
    )
    args = parser.parse_args()
    assert (args.url is None) ^ (args.urls_txt is None), "only one argparse needed"

    return args


def download(url_lst: List[str]):
    with youtube_dl.YoutubeDL() as ydl:
        ydl.download(url_lst)


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}


if __name__ == '__main__':
    args = get_args()
    urls = []
    if args.url:
        urls.append(args.url)
    elif args.urls_txt:
        with open(args.urls_txt, 'r') as f:
            urls = f.readlines()
    else:
        raise NotFoundErr("url path not found")

    download(urls)

    if args.output_dir:
        os.makedirs(args.output_dir, exist_ok=True)
        extensions = ['mp4', 'flv', 'webm', '3gp', 'm4a', 'mp3', 'ogg', 'aac', 'wav', 'mkv']
        for ext in extensions:
            os.system(f'mv *.{ext} {args.output_dir}')
