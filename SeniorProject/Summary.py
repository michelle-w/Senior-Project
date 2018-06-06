from requests import get
from contextlib import closing
from _codecs import decode
from _ast import Div
from PyDictionary import PyDictionary

class Summary:
    def __init__(self, html, summary, title):
        self.html = html
        self.summary = summary
        self.title = title
        self.science_terms = {}
        
    def print_summary(self):
        print("\n"+self.title)
        print("\n"+self.summary)
        
    
        
""" 
dictionary = PyDictionary()
definition = dictionary.meaning("embryo")
print(list(dictionary.meaning("embryo").values())[0])

string= "Hello my name is"
for word in string.split():
    print(word)
    
dict = {}
word = "Hi"
dict["Hi"] = None
print(dict)
"""
