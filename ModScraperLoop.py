'''This is the continuously running version, which goes through every section
with every function. If you don't want this program to run continuously, don't
run it from this file! '''
if __name__ == '__main__':
    import sys, os
    sys.path.append(os.getcwd()+'/Resources')
    import log_it
    import ModScraper
    from multiprocessing import Queue
    q = Queue()
    ModScraper.init(q)
    log_it.startLogging(q)
    log_it.logg("Startup successful", q, genus=["log"])

    while True: #this will continuously go until stopped by force
        ModScraper.main()
