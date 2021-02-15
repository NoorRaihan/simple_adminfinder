#author: NoorRaihan
import os
import requests

class warna:
   RED   = "\033[1;31m"
   GREEN = "\033[0;32m"



def linkfile():

    ask = raw_input("Guna default wordlist?: ")
    if ask == "Y" or ask == "y":
       urlfile = open("url.txt","r")
       r_url = urlfile.read().splitlines()
       return r_url
    
    elif ask == "N" or ask == "n":
        filepath = raw_input("Direktori File: ")
        urlfile = open(filepath,"r")
        r_url = urlfile.read().splitlines()
        return r_url

def checkurl():
       urlfile = linkfile()
       for link in urlfile:
          web = requests.get(site +link)
          resp = web.status_code
          if resp == 200:
             print warna.GREEN + "LINK VALID:"+link
          else:
             print warna.RED + "LINK INVALID:"+link


site = raw_input("Website(http://example.com/):")
checkurl()
