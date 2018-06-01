class Summary:
    def __init__(self, html, article, title):
        self.html = html
        self.article = article
        self.title = title
        
        self.scienceWords = []
        
    def print_summary(self):
        print("\n"+self.title)
        print("\n"+self.article)
        
    def find_science_words(self):
        for word in self.article.split():
            print(word)
            


