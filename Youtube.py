#!/bin/python3
import subprocess
import time


def main():
    place = "/home/neo/Téléchargements/"
    place = "/home/neo/Téléchargements/Youtube"
    urlplace = "/home/neo/Documents/youtube_url.txt"
    filetype = "mp3"
    subprocess.run(args=["pip3", "install", "youtube_dl",
                         "--upgrade", "--no-cache-dir"], check=True)
    while True:
        with open(urlplace, 'r+') as urlfile:
            urllist = urlfile.read().split('\n')
            for url in urllist:
                print(url)
                args = ["youtube-dl", "--add-metadata", "-x", "-q",
                        "--skip-unavailable-fragments", "--console-title",
                        "-i", "-o", "%(title)s.%(ext)s",
                        "--restrict-filenames", "--all-subs",
                        "--audio-format", filetype, url]
                # print(args)
                # subprocess.run(cwd=place, args=args, check=True)
                subprocess.run(cwd=place, args=args)
            urlfile.truncate(0)
        time.sleep(10)
        # break


if __name__ == "__main__":
    main()
