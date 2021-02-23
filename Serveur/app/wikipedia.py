#!/bin/python3
import wikipediaapi


def print_sections(sections, level=0):
    for s in sections:
        print("%s: %s - %s" % ("*" * (level + 1), s.title, s.text[0:40]))
        print_sections(s.sections, level + 1)


def print_langlinks(page):
    langlinks = page.langlinks
    for k in sorted(langlinks.keys()):
        v = langlinks[k]
        print("%s: %s - %s: %s" % (k, v.language, v.title, v.fullurl))


def print_links(page):
    links = page.links
    for title in sorted(links.keys()):
        print("%s: %s" % (title, links[title]))


def print_categories(page):
    categories = page.categories
    for title in sorted(categories.keys()):
        print("%s: %s" % (title, categories[title]))


def print_categorymembers(categorymembers, level=0, max_level=1):
    for c in categorymembers.values():
        print("%s: %s (ns: %d)" % ("*" * (level + 1), c.title, c.ns))
        if c.ns == wikipediaapi.Namespace.CATEGORY and level < max_level:
            print_categorymembers(
                c.categorymembers, level=level + 1, max_level=max_level)


wiki_wiki = wikipediaapi.Wikipedia(
    language='fr',
    extract_format=wikipediaapi.ExtractFormat.WIKI
)

if __name__ == "__main__":

    page_py = wiki_wiki.page('Python_(programming_language)')

    print("Page - Exists: %s" % page_py.exists())
    # Page - Exists: True

    page_missing = wiki_wiki.page('NonExistingPageWithStrangeName')
    print("Page - Exists: %s" % page_missing.exists())
    # Page - Exists: False

    print("Page - Title: %s" % page_py.title)

    print("Page - Summary: %s" % page_py.summary[0:60])
    # Page - Summary: Python is a widely used high-level programming language for

    print("fullurl : "+page_py.fullurl)
    print("canonicalurl : "+page_py.canonicalurl)

    print_langlinks(page_py)

    print_sections(page_py.sections)

    page_py_en = page_py.langlinks['en']
    print("Page - Summary: %s" % page_py_en.summary[0:60])

    print_links(page_py)

    print("Categories")
    print_categories(page_py)

    cat = wiki_wiki.page("Category:Physics")
    print("Category members: Category:Physics")
    print_categorymembers(cat.categorymembers)

    # print(page_py.text)
    print(page_py.summary)
