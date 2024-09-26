import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_subpages_from_url(base_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # Send a GET request to the base URL
        response = requests.get(base_url, headers=headers, timeout=10)
        response.raise_for_status()  # Check if the request was successful
        
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all <a> tags on the page
        links = soup.find_all('a', href=True)
        
        subpages = set()
        
        # Extract the subpage URLs
        for link in links:
            href = link['href']
            full_url = urljoin(base_url, href)
            
            # Filter links that belong to the base URL and are not external links
            if base_url in full_url:
                subpages.add(full_url)
        
        return list(subpages)
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

# Example usage
# base_url = "https://asvas-organization.gitbook.io/koboto-network-interface"
# subpages = get_subpages_from_url(base_url)

# print (len(subpages))
# print (subpages[1])
# Print the found subpages
# for subpage in subpages:
#     print(f"subpage 1: {subpage}")
