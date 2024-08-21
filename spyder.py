#!/usr/bin/env python
import requests
import re
def Request(url):
    try:
        return requests.get("http://" + url)
        
    except requests.exceptions.ConnectionError:
        pass
target_url = "adulttime.com"

response = Request(target_url)
if response:
    
    content = response.content.decode('utf-8', errors='ignore')
    
    
    href_links = re.findall(r'href=[\'"](.*?)[\'"]', content)
    
    for link in href_links:
        print(link)  
else:
    print("Failed to connect to the target URL")