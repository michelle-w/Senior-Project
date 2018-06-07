from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
from summa import summarizer
from _codecs import decode
from _ast import Div
from Summary import Summary
import re
import requests
from PyDictionary import PyDictionary

class ScienceSummarizer:
    
    def __init__(self):
        file = open("ScienceTerms.txt", "rt")
        self.terms = list(file.readlines())
 
    def is_good_response(self, resp):
        """returns true if response is HTML"""
        content_type = resp.headers['Content-Type'].lower()
        return (resp.status_code == 200 and content_type is not None and content_type.find('html') > -1)

    def log_error(self, e):
        print(e)
    
    def simple_get(self, url):
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
                if self.is_good_response(resp):
                    return resp.content
                else:
                    return None
        except RequestException as e:
            self.log_error('Error during requests to {0} : {1}'.format(url, str(e)))
            return None
    
    def get_html(self, raw_html):
        html = BeautifulSoup(raw_html, 'html.parser')
        return html
    
    def get_article(self, html):
        divs = html.find("div", {"class": "article__body serif cleared"})
        return divs.text
    
    def get_title(self, html):
        title = html.find("title")
        return title.text
    
    def unicodetoascii(self, text):
        TEXT = (text.
                replace('\\xe2\\x80\\x99', "'").
                replace('\\xc3\\xa9', 'e').
                replace('\\xe2\\x80\\x90', '-').
                replace('\\xe2\\x80\\x91', '-').
                replace('\\xe2\\x80\\x92', '-').
                replace('\\xe2\\x80\\x93', '-').
                replace('\\xe2\\x80\\x94', '-').
                replace('\\xe2\\x80\\x94', '-').
                replace('\\xe2\\x80\\x98', "'").
                replace('\\xe2\\x80\\x9b', "'").
                replace('\\xe2\\x80\\x9c', '"').
                replace('\\xe2\\x80\\x9c', '"').
                replace('\\xe2\\x80\\x9d', '"').
                replace('\\xe2\\x80\\x9e', '"').
                replace('\\xe2\\x80\\x9f', '"').
                replace('\\xe2\\x80\\xa6', '...').#
                replace('\\xe2\\x80\\xb2', "'").
                replace('\\xe2\\x80\\xb3', "'").
                replace('\\xe2\\x80\\xb4', "'").
                replace('\\xe2\\x80\\xb5', "'").
                replace('\\xe2\\x80\\xb6', "'").
                replace('\\xe2\\x80\\xb7', "'").
                replace('\\xe2\\x81\\xba', "+").
                replace('\\xe2\\x81\\xbb', "-").
                replace('\\xe2\\x81\\xbc', "=").
                replace('\\xe2\\x81\\xbd', "(").
                replace('\\xe2\\x81\\xbe', ")").
                replace("\\'", "'")
    
                     )
        return TEXT
    
    def get_summary(self, url):
        raw_html = self.simple_get(url)
        
        print(len(raw_html))
    
        #Get article and summarize it
        html = self.get_html(str(raw_html))
        article = self.get_article(html)
        title = self.get_title(html)
        
        summ = Summary(html, summarizer.summarize(self.unicodetoascii(article)), self.unicodetoascii(title).title())
        return summ
    
    def get_science_terms(self, summ):
        for i in range(0, len(self.terms)):
            self.terms[i] = self.terms[i].split("\n")[0]
        
        for word in summ.summary.split():
            if word in self.terms:
                summ.science_terms[word] = None
            else:
                pass
                
    def get_definitions(self, summ):
        dictionary = PyDictionary()
        for term in summ.science_terms:
            definition = list(dictionary.meaning(term).values())
            summ.science_terms[term] = definition
    
    def get_hyperlinks(self, url):
        raw_html = self.simple_get(url)
        
        print(len(raw_html))
    
        #Get article and summarize it
        html = self.get_html(str(raw_html))
        for link in html.find_all('a'):
        current_link = link.get('href')
        if current_link is not None:
            if current_link.find("news/") is not -1:
                news_hyperlinks.append(current_link)
        for num in range(len(news_hyperlinks)):
            print (news_hyperlinks[num])

scisumm = ScienceSummarizer()
summ = scisumm.get_summary("https://www.nature.com/articles/d41586-018-05357-w")
summ.print_summary()
scisumm.get_science_terms(summ)
scisumm.get_definitions(summ)
summ.print_summary()
scisumm.get_hyperlinks("https://www.nature.com")
