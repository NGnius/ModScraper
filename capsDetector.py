'''Detects caps'''

def isCaps(string, threshold = 1): #find capitalised parts of a string
    #returns True if the number of capitalised letters is greater than/equal to the threshold
    output = False
    capsCount = 0
    for char in string:
        if char.lower() != char:
            capsCount +=1
        if capsCount >= threshold:
            output = True
            break
    return output

def isCapsTitle(post, threshold, mode="boolean"): #detect if the title of a post is all caps
    output = False
    title = post.findTopicTitle()
    if threshold >= 0: #if threshold number is less than 0, add the amount to the string length
        isCapsResult = isCaps(title, threshold = threshold)
    else:
        isCapsResult = isCaps(title, threshold = len(title)+threshold)

    if isCapsResult:
        if mode == "boolean":
            output = True
        if mode == "link":
            output = postLink
        if mode == "title":
            output = title
    return output
