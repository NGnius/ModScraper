def isCrusher(post):
    '''(pageClass) -> bool
    returns True if there is any mention of crusher in the post, False otherwise'''
    if len(post.search(post.text, "crusher")) > 0 or len(post.search(post.text, "Crusher4881")) > 0:
        return True
    else:
        return False

def isRotatingPlatforms(post):
    '''(pageClass) -> bool
    returns True is that horrible video link is found, False otherwise'''
    if len(post.search(post.raw, "https://www.youtube.com/watch?v=uyEyppnE9c4&t=2s")) > 0 or len(post.search(post.raw, "https://youtu.be/uyEyppnE9c4")) > 0:
        return True
    else:
        return False
