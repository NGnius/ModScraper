import configparser, os
config = configparser.ConfigParser()
loadedConfig = {}
def loadConfig(): #load the config.txt files
    config.read(os.getcwd()+"/Resources/config.txt")

def appropriateType(string):
    if string.isnumeric(): #if string is a number
        return int(string)
    elif string[1:].isnumeric() and string[0] == "-": #if string is negative number
        return -int(string[1:])
    elif string.lower()[0]=="y" and len(string)<= len("yes"): #if string is close to "yes"
        return True
    elif string.lower()[0]=="n" and len(string)<= len("no"): #if string is close to "no"
        return False
    elif string[:-1].isnumeric(): #if string is a time
        if string[-1].lower() == "s": #seconds
            return int(string[:-1])
        elif string[-1].lower()=="h": #hours
            return int(string[:-1])*60*60
        elif string[-1].lower()=="d": #days
            return int(string[-1:])*60*60*24
        elif string[-2:].lower()=="mo": #months
            return int(string[:-2])*60*60*24*(365/12)
        elif string[-1:].lower()=="y": #years
            return int(string[:-1])*60*60*24*365
    elif string[:-2].isnumeric(): #if string is a time (cont'd) (if has mi or mo ending)
        if string[-2:].lower()=="mi": #minutes
            return int(string[:-2])*60
        elif string[-2:].lower()=="mo": #months
            return int(string[:-2])*60*60*24*(365/12)
    else:
        return string.lower()

def retrieveConfig(key): #search through the sections of the config to try and find key
    if key in loadedConfig:
        return loadedConfig[key]
    elif key in config["custom"]:
        loadedConfig[key] = appropriateType(config["custom"][key])
        return loadedConfig[key]
    elif key in config["DEFAULT"]:
        loadedConfig[key] =  appropriateType(config["DEFAULT"][key])
        return loadedConfig[key]
    else:
        print("Invalid Key")
        return None

loadConfig()
