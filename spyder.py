#!/usr/bin/env python
import requests
import re
from urllib.parse import urljoin
import time

target_url = "http://pornhat.one"
target_links = []
request_delay = 2  # Delay between requests in seconds

def extract_links_from(url):
    try:
        # Set a timeout for the request (e.g., 10 seconds)
        response = requests.get(url, timeout=10)
        # Decode response content to ensure proper string handling
        return re.findall(r'href="(.*?)"', response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []

def crawl(url):
    href_links = extract_links_from(url)
    for link in href_links:
        link = urljoin(url, link)
        if "#" in link:
            link = link.split('#')[0]
        if target_url in link and link not in target_links:
            target_links.append(link)
            print(link)
            time.sleep(request_delay)  # Throttle the requests
            crawl(link)

crawl(target_url)
