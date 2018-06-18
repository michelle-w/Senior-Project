'''
Created on May 22, 2018

@author: shobh
'''

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from ScienceSummarizer import ScienceSummarizer
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty


class IntroScreen(Screen):
    pass

class SummariesScreen(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.summary_index = 0
        self.scisumm = ScienceSummarizer()
        self.scisumm.get_hyperlinks("https://www.nature.com/news")
        link = self.scisumm.news_hyperlinks[self.summary_index]
        self.summ = self.scisumm.get_summary(link)
        self.s = self.summ.summary
        self.t = self.summ.title
    
    def change_summaries(self):
        print("running change summary")
        self.summary_index+= 1
        print(self.summary_index)
        link = self.scisumm.news_hyperlinks[self.summary_index]
        self.summ = self.scisumm.get_summary(link)
        label1= self.ids['label1']
        label2 = self.ids['label2']
        self.s = self.summ.summary
        self.t = self.summ.title
        label1.text = self.t
        label2.text= self.s
    
    def dict_to_str(self, di):
        st = ""
        for key in di:
            st += "  "
            st += key.upper()
            st += ": "
            for de1 in di[key]:
                for de2 in de1:
                    st += de2
                    st += "; "
        return st
    
    def show_defs(self):
        print("running show defs")
        label2= self.ids['label2']
        label2.text = self.dict_to_str(self.summ.science_terms)
    
    

class ScreenManagement(ScreenManager):
    pass


class MainApp(App):
            
    def build(self):
        pass
if __name__=="__main__":
    MainApp().run()
