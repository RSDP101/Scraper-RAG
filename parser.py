import requests
from bs4 import BeautifulSoup
from get_subpages import get_subpages_from_url
def get_text_from_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # Send a GET request to the URL with headers and a timeout of 10 seconds
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Check if the request was successful
        
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract the main text by selecting all <p> tags
        paragraphs = soup.find_all('p')
        text = ' '.join([p.get_text() for p in paragraphs[:50]])  # Limiting to the first 50 paragraphs
        
        return text
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

def get_all_texts(base_url):
    subpages = get_subpages_from_url(base_url)
    all_texts_from_pages = []
    for page in subpages:
        # print ("scraping page")
        text = get_text_from_url(page)
        all_texts_from_pages.append(text)
    return all_texts_from_pages


# Example usage
# base_url = "https://asvas-organization.gitbook.io/koboto-network-interface"
# all_texts = get_all_texts(base_url)

