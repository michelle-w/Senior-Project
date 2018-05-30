from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
from summa import summarizer
from _codecs import decode
from _ast import Div

def is_good_response(resp):
    """returns true if response is HTML"""
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 and content_type is not None and content_type.find('html') > -1)

def log_error(e):
    print(e)

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None
    """
    """
    The simple_get function accepts a single url argument. 
    It then makes a GET request to that url. 
    If nothing goes wrong, you end up with the raw HTML content for the page you requested. 
    If there were any problems with your request (like the url is bad or the remote server is down) 
    then your functon returns None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None
    

def get_article(filename):
    html_file= open(filename, 'rt')
    raw_html = html_file.read()
    html = BeautifulSoup(raw_html, 'html.parser')
    
    divs = html.find("div", {"class": "article__body serif cleared"})
    return divs.text



#simple_get test
raw_html = simple_get("https://www.nature.com/articles/d41586-018-05278-8")
print(len(raw_html))
output_file = open("htmlOutput.txt", "w+", encoding='utf-8')
output_file.write(str(raw_html))
output_file.close()

#Get article and summarize it
article = get_article('htmlOutput.txt')
print(summarizer.summarize(article))
"""Sources that allow article extraction:
 -Science News
 -Scientific American
 -Science journal
 -BBC news science news
 -Nature news articles
 
 Sources that don't seem to allow:
  - Science Daily
  -phys.org
"""