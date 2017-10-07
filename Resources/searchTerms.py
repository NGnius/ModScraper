import scraper, os

def loadTerms():
    '''() -> list
    loads each line of searchterms.txt as a seperate term'''
    terms = scraper.fileIO.retrieveFileLines(os.getcwd()+"/Resources/searchterms.txt")
    output = []
    for i in range(len(terms)):
        terms[i] = terms[i].strip(" \n,.\t")
        terms[i] = terms[i].lower()
        if len(terms[i])>1:
            output.append(terms[i])
    return output
