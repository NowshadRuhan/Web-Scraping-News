import requests
from bs4 import BeautifulSoup
import json

# URL of the website to scrape
url = 'https://en.prothomalo.com/'

# Sending a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parsing the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Finding all the heading elements (h1, h2, h3, h4, h5, h6)
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    
    # Extracting the text of the headings and creating a list of headings
    heading_texts = [heading.text.strip() for heading in headings]
    
    # Creating a dictionary to store the heading data
    heading_data = {'headings': heading_texts}
    
    # Saving the heading data to a JSON file
    with open('headings.json', 'w', encoding='utf-8') as file:
        json.dump(heading_data, file, ensure_ascii=False, indent=4)
    
    print('Heading data saved to headings.json')
else:
    print('Failed to retrieve the web page.')
