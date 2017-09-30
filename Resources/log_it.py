'''Custom logging module'''
import sys, os, time
sys.path.append(os.getcwd()+'/scraperResources')
import fileIO
sys.path.append(os.getcwd()+'/Resources')
import config
filename="log.txt"
from multiprocessing import Process

def timestamp():
    '''() -> str
    creates a pretty timestamp'''
    localtime = time.localtime()
    return "[" + str(localtime.tm_mday) + "/" + str(localtime.tm_mon) + "/" + str(localtime.tm_year) + " at " + str(localtime.tm_hour) + ":" + str(localtime.tm_min) + ":" + str(localtime.tm_sec) + "]"

def savetologg(string, genus=["debug"]):
    '''(str, list of str) -> None
    write to the log'''
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
    '''(Queue object) -> None
    continuously run savetologg (preferably in a seperate process)'''
    while True:
        tolog = pipe_conn.get()
        savetologg(tolog[0], tolog[1])

def startLogging(logg_conn):
    '''(Queue object) -> None
    start loggingThread as a multiprocessing Process'''
    fileIO.addToFile(filename, timestamp()+"Starting up...\n", overwrite=True) #overwrite log file if it already exists, create it if not
    savetologg("Received queue, starting logging thread", genus=["debug"])
    p = Process(target=loggingThread, args=(logg_conn,))
    p.start()
