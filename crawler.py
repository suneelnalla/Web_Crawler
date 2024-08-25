# #!/usr/bin/env python
import requests

def request(url):
    """Send an HTTP GET request and return the response if successful, otherwise return None."""
    try:
        response = requests.get("http://" + url)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException:
        return None

def discover_subdomains(target_url, subdomains_wordlist):
    """Discover subdomains by checking each entry in the subdomains wordlist."""
    discovered_subdomains = []
    with open(subdomains_wordlist, "r") as wordlist_file:
        for line in wordlist_file:
            subdomain = line.strip()
            test_url = f"{subdomain}.{target_url}"
            response = request(test_url)
            if response:
                print(f"[+] Discoverable subdomain --> {test_url}")
                discovered_subdomains.append(test_url)
    return discovered_subdomains

def discover_files_and_directories(target_url, files_and_dirs_wordlist):
    """Discover files and directories on the target URL and its subdomains."""
    with open(files_and_dirs_wordlist, "r") as wordlist_file:
        for line in wordlist_file:
            path = line.strip()
            # Check main domain
            test_url = f"http://{target_url}/{path}"
            response = request(test_url)
            if response and response.status_code == 200:
                print(f"[+] Discoverable file or directory on main domain --> {test_url}")

            # Check subdomains
            subdomains = discover_subdomains(target_url, subdomains_wordlist)
            for subdomain in subdomains:
                test_url = f"http://{subdomain}/{path}"
                response = request(test_url)
                if response and response.status_code == 200:
                    print(f"[+] Discoverable file or directory on subdomain --> {test_url}")

if __name__ == "__main__":
    target_url = ""
    subdomains_wordlist = "D:/python_scripts/web_crawler/subdomains-wodlist2.txt"
    files_and_dirs_wordlist = "D:/python_scripts/web_crawler/files-and-dirs-wordlist.txt"

    # Discover files and directories on the main domain and subdomains
    discover_files_and_directories(target_url, files_and_dirs_wordlist)
