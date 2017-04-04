import sys, os
sys.path.append(os.getcwd()+'/scraperResources')
import pageRet, fileIO, wordSearcher, findFirstPost
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
    def findFirstPost(self):
        return findFirstPost.FirstPost(self.raw)
page = pageClass()

def find(string):
    return wordSearcher.wordSearcher(string, page.text)

