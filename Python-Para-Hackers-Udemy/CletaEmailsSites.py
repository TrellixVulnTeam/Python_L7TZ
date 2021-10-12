import requests
import re
import time

SiteList = ["https://www.cooxupe.com.br"]
def GetEmailBySItes(SiteList):
    for i in SiteList:
        DataSite = requests.get(i)
        print (DataSite)
        ReturnRegex = re.findall(f'[\w\.-]+@[\w\.-]+\.\w*',DataSite.text)
        if ReturnRegex:
            return (list(set(ReturnRegex)))
        else:
            return None

sites= ["https://www.cooxupe.com.br"]

cont_x=0

try:
    for x in sites:
        mails=(GetEmailBySItes(x))
        if (mails != "None" or mails != None):
            print(mails)
        cont_x=cont_x+1
except:
    print (x)
    pass