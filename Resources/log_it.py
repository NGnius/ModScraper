'''Logging module'''
import sys, os, time
sys.path.append(os.getcwd()+'/scraperResources')
import fileIO
filename="log.txt"
fileIO.addToFile(filename,"Starting up...\n", overwrite=True)
run = True

def timestamp():
    localtime = time.localtime()
    return "[" + str(localtime.tm_mday) + "/" + str(localtime.tm_mon) + "/" + str(localtime.tm_year) + " at " + str(localtime.tm_hour) + ":" + str(localtime.tm_min) + ":" + str(localtime.tm_sec) + "]"

def logg(string): #write to the log
    fileIO.addToFile(filename, timestamp()+string+"\n")
