def main():
    import os

    def url_exists(url):
        commande = 'ping -c 1 "' + url + '"'
        response = os.system(commande)
        # and then check the response...
        if response == 0:
            return True
        else:
            return False

    print(url_exists("yaya.cout.free.fr"))


if __name__ == "__main__":
    main()
