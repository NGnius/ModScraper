import wordSearcher
def findTitle(rawpage, mode="string"):
    titleStart = wordSearcher.wordSearcher("<title>", rawpage, output="lastchar")[0]
    titleEnd = wordSearcher.wordSearcher("</title>", rawpage[titleStart:])[0]+titleStart
    if mode == "string":
        return rawpage[titleStart:titleEnd]
    elif mode == "range":
        return titleStart, titleEnd
