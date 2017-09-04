'''Logging module'''
import sys, os, time
sys.path.append(os.getcwd()+'/scraperResources')
import fileIO
sys.path.append(os.getcwd()+'/Resources')
import config
filename="log.txt"
from multiprocessing import Process

def timestamp():
    localtime = time.localtime()
    return "[" + str(localtime.tm_mday) + "/" + str(localtime.tm_mon) + "/" + str(localtime.tm_year) + " at " + str(localtime.tm_hour) + ":" + str(localtime.tm_min) + ":" + str(localtime.tm_sec) + "]"

def savetologg(string, genus=["debug"]): #write to the log
    isin = True
    for item in genus: #check for genuses in loggenuses
        if item not in config.retrieveConfig("loggenuses"):
            isin = False
            break
    if isin or "log" in genus:
        fileIO.addToFile(filename, timestamp()+string+"\n")
    isin = True
    for item in genus: #check for genuses in printgenuses
        if item not in config.retrieveConfig("printgenuses"):
            isin = False
            break
    if isin or "print" in genus:
        print(timestamp()+string)

def logg(string, conn, genus=["debug"]):
    conn.put([string, genus])

def loggingThread(pipe_conn):
    while True:
        tolog = pipe_conn.get()
        savetologg(tolog[0], tolog[1])

def startLogging(logg_conn):
    p = Process(target=loggingThread, args=(logg_conn,))
    p.start()

fileIO.addToFile(filename, timestamp()+"Starting up...\n", overwrite=True) #overwrite log file if it already exists, create it if not
