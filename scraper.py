import sys, os
sys.path.append(os.getcwd()+'/scraperResources')
import pageRet, fileIO, wordSearcher, findPosts, findDates
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
    def findFirstPost(self): #find first post in a forum section
        return findPosts.FirstPost(self.raw)
    def findAllPosts(self): #find all posts in a forum section
        return findPosts.FindPosts(self.raw)
    def findDates(self): #find all post dates in a post
        return findDates.findDates(self.text)
page = pageClass()

def find(string):
    return wordSearcher.wordSearcher(string, page.text)
