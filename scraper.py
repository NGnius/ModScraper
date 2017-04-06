import sys, os
sys.path.append(os.getcwd()+'/scraperResources')
import pageRet, fileIO, wordSearcher, findFirstPost, findDates
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
    def findDates(self):
        return findDates.findDates(self.text)
page = pageClass()

def find(string):
    return wordSearcher.wordSearcher(string, page.text)

