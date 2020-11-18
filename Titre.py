def main():
    # import re
    import requests
    import xml.etree.ElementTree as ET

    def parseXML(xmlfile):
        # create element tree object
        tree = ET.parse(xmlfile)

        # get root element
        root = tree.getroot()

        # create empty list for news items
        newsitems = []

        for item in root.findall("./"):
            # print(list(item))
            # empty news dictionary
            news = {}
            # print(item.text)
            readxml(item, news, newsitems)
            # print(dir(item))

        # return news items list
        return newsitems

    def readxml(item, news, newsitems):
        # iterate child elements of item
        for child in item:
            # print(list(child))
            if child.text is None or "  " in child.text or "    " in\
                    child.text or "//" in child.text:
                pass
                # print("coucou")
            else:
                pass
                print(child.text)
            # print(dir(child.))
            try:
                newsitems = readxml(child, news, newsitems)
            except Exception:
                pass
            # news[child.tag] = child.text.encode('utf8')
            # append news dictionary to news items list
            newsitems.append(news)
        # return news items list
        return newsitems

    # parseXML('/home/neo/Documents/Python/topnewsfeed.xml')
    n = requests.get('https://yaya.cout.free.fr')
    print(n.content)
    # with open('Page.html', 'wb') as f:
    #     f.write(n.content)
    #     print(open('Page.html'))
    # parseXML('topnewsfeed.xml')
    parseXML('Page.html')

    # with open('Page.html', 'wb') as f:
    #     # f.write(n)
    #     print(f)
    #     match = re.search('<title>(.*?)</title>', f)


if __name__ == "__main__":
    main()
