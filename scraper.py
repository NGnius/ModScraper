import sys, os
sys.path.append(os.getcwd()+'/scraperResources')
import pageRet, fileIO, wordSearcher, findPosts, findDates, findTitle
class pageClass:
    def ret(self, url):
        self.raw = pageRet.pageRet(url).decode()
        self.url = url
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
    def findTitle(self):
        return findTitle.findTitle(self.raw)
    def findTopicTitle(self):
        fullTitle = self.findTitle()
        topicTitle = fullTitle[wordSearcher.wordSearcher(" Topic: ", fullTitle, output="lastchar")[0]:]
        return topicTitle
    def searchraw(self, string):
        return wordSearcher.wordSearcher(string, self.raw)
    def searchtext(self, string):
        return wordSearcher.wordSearcher(string, self.text)
page = pageClass()

def find(string):
    return wordSearcher.wordSearcher(string, page.text)
