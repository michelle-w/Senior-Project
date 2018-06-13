'''
Created on May 22, 2018

@author: shobh
'''

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from ScienceSummarizer import ScienceSummarizer


class IntroScreen(Screen):
    pass

class SummariesScreen(Screen):
    summaries=[]
    scisumm = ScienceSummarizer()
    scisumm.get_hyperlinks("https://www.nature.com/news")
    link = scisumm.news_hyperlinks[0]
    summ = scisumm.get_summary(link)
    s = summ.summary
    pass

class ScreenManagement(ScreenManager):
    pass


class MainApp(App):
            
    def build(self):
        return Builder.load_file("main.kv")

MainApp().run()
