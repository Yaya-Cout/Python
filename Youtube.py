def main():
    import os
    import subprocess
    import time
    place = "/home/neo/Téléchargements/"
    place = "/home/neo/Téléchargements/Youtube"
    urlplace = "/home/neo/Documents/youtube_url.txt"
    filetype = "mp3"
    while True:
        subprocess.run(args=["pip3", "install", "youtube_dl",
                             "--upgrade", "--no-cache-dir"])
        url = os.popen("cat " + urlplace).read()
        urllist = url.split('\n')
        for url in urllist:
            print(url)
            args = ["youtube-dl", "--add-metadata", "-x", "-q",
                    "--skip-unavailable-fragments", "--console-title", "-i",
                    "-o", '%(title)s.%(ext)s', "--restrict-filenames", *
                    "--all-subs", "--audio-format", filetype, url]
            # print(args)
            subprocess.run(cwd=place, args=args)
        time.sleep(10)
        # break


if __name__ == "__main__":
    main()
