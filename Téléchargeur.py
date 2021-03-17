def main():
    import requests

    url = "http://yaya.cout.free.fr/"
    while True:
        url = input("Votre URL : ")
        resp = requests.get(url)
        with open("Page.html", "wb") as f:
            f.write(resp.content)


if __name__ == "__main__":
    main()
