from bs4 import BeautifulSoup
import requests as req
import re

def fetch_currency(amount, sc, tc):
    '''amount = 100
    sc = 'INR'
    tc = 'GBP'''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': 'https://google.com',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    url = f'https://www.google.com/search?q=convert {amount} {sc} to {tc}'
    r = req.get(url, headers=headers)

    soup = BeautifulSoup(r.content, 'html.parser')
    stuff = soup.find_all('div', class_='dDoNo')

    pattern = r'<span class="DFlfde SwHCTb" data-precision="\d+" data-value="([\d.]+)">'

    # Use re.search() to find the match
    match = re.search(pattern, str(stuff))

    # Check if a match is found
    if match:
        # Extract the matched value
        converted_currency = match.group(1)
    return converted_currency