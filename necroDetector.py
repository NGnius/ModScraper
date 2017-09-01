'''Detect threads that have been bumped from the dead'''
import time

def timeDelta(a,b): #subtracts the time, in seconds, between struct_time a and b
    return abs( (((b.tm_year*365)+b.tm_yday)*24*60*60) - (((a.tm_year*365)+a.tm_yday)*24*60*60) )

def isNecro(post, delta, mode = "boolean"): #detect if post has been necroed
    #boolean mode returns True if the post has been necroed, False if not
    #link mode returns postLink if the post has been necroed, False if not
    output = False
    dates = post.findDates() #find all the post and reply dates in the post
    #check if the years match for first and last post as well as last and second last post and set output appropriately
    if len(dates)>1: #to prevent the module from crashing if the thread has only one post in it (it's a new thread and only has the OP's 1st post)
        if timeDelta(dates[-2][0], dates[-1][0])>delta:
            #print ("Boop: We have a necro from ", postLink) #don't ask; printing weird things is more fun
            if mode == "boolean":
                output = True
            if mode == "link":
                output = post.url
    return output
