import requests
from bs4 import BeautifulSoup

def extract_article_content(url):
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for HTTP errors
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all paragraph tags (common for news articles)
        paragraphs = soup.find_all('p')
        content = ' '.join(para.get_text() for para in paragraphs if para.get_text().strip())
        
        return content if content else "No content found."
    except requests.exceptions.RequestException as e:
        return f"HTTP Error: {str(e)}"
