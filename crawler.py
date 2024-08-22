#!/usr/bin/env python
import requests

def Request(url):
    try:
        return requests.get("http://" + url)
        
    except requests.exceptions.ConnectionError:
        pass
target_url = "google.com"
with open("D:\python_scripts\web_crawler\subdomains-wodlist.txt.txt","r") as wordlist_file:

    for line in wordlist_file:
        word = line.strip()
        test_url = word + "." + target_url
        print(test_url)
with open("D:/python_scripts/web_crawler/files-and-dirs-wordlist.txt","r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = target_url + "/" + word
        response = Request(test_url)
        if response:
            print("[+] Discoverable subdomain -->" + test_url)
 
