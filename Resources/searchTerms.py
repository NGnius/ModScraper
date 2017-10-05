import scraper, os

def loadTerms():
    terms = scraper.fileIO.retrieveFileLines(os.getcwd()+"/Resources/searchterms.txt")
    for i in range(len(terms)):
        terms[i] = terms[i].strip(" \n,.\t")
        terms[i] = terms[i].lower()
    return terms
