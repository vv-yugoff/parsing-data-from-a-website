import requests
from bs4 import BeautifulSoup

# Creating a request header specifying the User-Agent so that the site does not block requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Sending a GET request to the main page
response = requests.get("https://2gis.ru", headers=headers)

# Creating a BeautifulSoup object to analyze the HTML code of the response
soup = BeautifulSoup(response.content, 'html.parser')

# We find all the elements with the "mini-card-title" class. Each element represents information about a bath, sauna, steam room or hammam
card_titles = soup.find_all(class_="mini-card-title")

# We sort through the elements and output the information contained in them
for title in card_titles:
    print(title.text.strip())