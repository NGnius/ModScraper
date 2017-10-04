def isCrusher(post):
    '''(pageClass) -> bool
    returns True if there is any mention of crusher in the post, False otherwise'''
    if len(post.searchtext("crusher")) > 0 or len(post.searchtext("Crusher4881")) > 0:
        return True
    else:
        return False

def isRotatingPlatforms(post):
    '''(pageClass) -> bool
    returns True is that horrible video link is found, False otherwise'''
    if len(post.searchraw("https://www.youtube.com/watch?v=uyEyppnE9c4")) > 0 or len(post.searchraw("https://youtu.be/uyEyppnE9c4")) > 0 or len(post.searchraw("uyEyppnE9c4")):
        return True
    else:
        return False
