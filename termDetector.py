import searchTerms

def containsTerm(post, mode="boolean"):
    '''(pageClass) -> bool or list
    boolean mode returns True if at least one term is found in the post
    list mode returns a list of all terms found in the post'''
    foundTerms = []
    for i in terms:
        if len(post.search(i, post.text.lower())) > 0: #post.text.lower() may be a bad idea with a huge string, but idc
            foundTerms.append(i)
    if mode == "boolean":
        return len(foundTerms) > 0
    elif mode == "list":
        return foundTerms

terms = searchTerms.loadTerms()
