def main():
    import webbrowser
    import time
    import random

    def ouvrir(URL):
        webbrowser.open(URL+str(random.randint(0, 255)))
        print(time.time())
        opened = + 1
        print(opened)
        time.sleep(2)

    while True:
        ouvrir("https://www.qwant.com/?q=")
        ouvrir("https://www.ecosia.org/search?q=")


if __name__ == "__main__":
    main()
