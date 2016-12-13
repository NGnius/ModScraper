import sys, os
sys.path.append(os.getcwd()+'/resources')
import pageRet, fileIO, wordSearcher
class pageClass:
    def ret(self, url):
        self.raw = pageRet.pageRet(url).decode()
        ignoreChars = False
        text = ""
        for char in self.raw:
            if char == "<":
                ignoreChars = True
            elif char == ">":
                ignoreChars = False
            elif not ignoreChars:
                text += str(char)
        self.text = text
page = pageClass()

def find(string):
    return wordSearcher.wordSearcher(string, page.text)

