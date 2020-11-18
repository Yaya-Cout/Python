# Python code to illustrate parsing of XML files
# importing the required modules
import csv
import requests
import xml.etree.ElementTree as ET
# url of rss feed
url = 'http://yaya.cout.free.fr/Rss.php'


def loadRSS():

    # creating HTTP response object from given url
    resp = requests.get(url)

    # saving the xml file
    with open('topnewsfeed.xml', 'wb') as f:
        f.write(resp.content)
        return f


def parseXML(xmlfile):
    # create element tree object
    tree = ET.parse(xmlfile)

    # get root element
    root = tree.getroot()

    # create empty list for news items
    newsitems = []

    # iterate news items
    for item in root.findall('./channel/item'):

        # empty news dictionary
        news = {}

        # iterate child elements of item
        for child in item:
            # print(child.text.encode('utf8'))
            news[child.tag] = child.text.encode('utf8')

        # append news dictionary to news items list
        newsitems.append(news)
    # return news items list
    return newsitems


def check_new(file, filename):
    # with open('topnewsfeed.xml') as f:
    #     # f.write(resp.content)
    #     requete = f
    if requests.get(url) == file:
        return False
    else:
        return True


def savetoCSV(newsitems, filename):

    # specifying the fields for csv file
    fields = ['guid', 'title', 'pubDate',
              'description', 'link', 'media', 'author']

    # writing to csv file
    with open(filename, 'w') as csvfile:

        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=fields)

        # writing headers (field names)
        writer.writeheader()

        # writing data rows
        writer.writerows(newsitems)


def main():
    # load rss from web to update existing xml file
    loadRSS()

    # parse xml file
    newsitems = parseXML('topnewsfeed.xml')

    # check new items
    save = check_new(newsitems, 'topnews.csv')
    print(save)
    save = True
    if save:
        # store news items in a csv file
        savetoCSV(newsitems, 'topnews.csv')
    else:
        print("Pas de nouvel article.")


if __name__ == "__main__":

    # calling main function
    main()


# import requests
# import xml.etree.ElementTree as ET

# # url of news rss feed
# RSS_FEED_URL = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"

# def loadRSS():
#     '''
#     utility function to load RSS feed
#     '''
#     # create HTTP request response object
#     resp = requests.get(RSS_FEED_URL)

#     # return response content
#     return resp.content

# def parseXML(rss):
#     '''
#     utility function to parse XML format rss feed
#     '''
#     # create element tree root object
#     root = ET.fromstring(rss)

#     # create empty list for news items
#     newsitems = []

#     # iterate news items
#     for item in root.findall('./channel/item'):
#         news = {}

#         # iterate child elements of item
#         for child in item:

#             # special checking for namespace object content:media
#             if child.tag == '{http://search.yahoo.com/mrss/}content':
#                 news['media'] = child.attrib['url']
#             else:
#                 news[child.tag] = child.text.encode('utf8')
#         newsitems.append(news)

#     # return news items list
#     return newsitems

# def topStories():
#     '''
#     main function to generate and return news items
#     '''
#     # load rss feed
#     rss = loadRSS()

#     # parse XML
#     newsitems = parseXML(rss)
#     return newsitems
