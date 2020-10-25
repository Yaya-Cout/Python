def main():
    import pyperclip
    import time
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="File to save",
                        default="/home/neo/Documents/clipboard.txt")
    args = parser.parse_args()
    clipbord_place = args.file

    while True:
        clipboard = pyperclip.paste()
        with open(clipbord_place, "a") as file_write:
            with open(clipbord_place, "r") as file_read:
                file_content = file_read.read()
                if clipboard in file_content:
                    pass
                else:
                    file_write.write("\n" + clipboard)
                time.sleep(1)


if __name__ == "__main__":
    main()
