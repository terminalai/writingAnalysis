import requests
from bs4 import BeautifulSoup as souper

__all__ = [
    "nytimes",
    "nature",
    "forbes",
    "functions"
]

def _findClass(tag):
    """
    Yes, this a display of bad programming practices by our very own Prannaya Gupta.

    Don't worry, it's just a way of saying that BeautifulSoup kinda sucks big time.

    :param tag: Simply the BeautifulSoup Tag Object

    :returns: An iterable or a string containing the combination of, or simply the singular, class defined by the news site creator.
    """
    try: return tag["class"]
    except KeyError: return []

def nytimes(url):
    """
    We tried to retrieve text from the New York Times, which is pretty useful since a lot of what they write is pure gold.
    We simply compile a list of urls and retrieve the articles by means of applying it on every url.
    This is certainly not the best way, but it is the way we have to go with since there is no real corpus of New York Times articles,
    These files are later stored individually in separate text files, due to the use of newlines.

    :param url: New York Times Article URL
    :returns: A multi-line string containing all the text from the article.
    """
    return "\n\n".join([tag.text for tag in souper(requests.get(url).content).findAll("p", {"class":"evys1bk0"})])


def nature(url):
    """
    Yes, apparently Nature has an Opinion section. And it's crazily formatted.
    Anyways, we get another function to retrieve the markdown files this time.

    :param url: A Nature Opinion Article URL
    :returns: A multi-line markdown-formatted string containing all the text from the article.
    """
    return "\n\n".join([(i.name=="h2")*"##" + i.text.strip() for i in souper(requests.get(url).content).findAll("div", {"class":"c-article-body"})[0].findChildren(recursive=False) if "recommended" not in _findClass(i)])


def forbes(url):
    """
    I don't know why Forbes is here, I was using it for EL5132 and kind created on for Forbes too.

    :param url: A Forbes Article URL
    :returns: A multi-line string containing all the text from the article.
    """
    return "\n\n".join([tag.text.strip() for tag in souper(requests.get(url).content).find("div", {"class":"article-body"}).findAll("p") if "wp-caption-text" not in _findClass(tag)])


#souper(requests.get("https://www.linkedin.com/pulse/hirings-new-red-line-why-newcomers-cant-land-35-jobs-george-anders/").content).find("div", {"class":"reader-article-content"})



functions = [nytimes, nature, forbes]



