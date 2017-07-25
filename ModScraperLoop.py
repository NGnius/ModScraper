'''This is the continuously running version, which goes through every section
with every function. If you don't want this program to run continuously, don't
run it from this file! '''
import sys, os
sys.path.append(os.getcwd()+'/Resources')
import ForumsToCheck, wordSearcher, scraper, necroDetector, profanityDetector, ModScraper

while True: #this will continuously go until stopped by force
    ModScraper.main()
