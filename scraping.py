import requests
from bs4 import BeautifulSoup

# URL til nettsiden vi skal scrape
url = 'http://quotes.toscrape.com'

# Send en GET-forespørsel til nettsiden
response = requests.get(url)

# Hent HTML-innholdet fra responsen
html_content = response.text

# Bruk BeautifulSoup for å parse HTML-en
soup = BeautifulSoup(html_content, 'html.parser')

# Finn alle <div>-elementer med klassen "quote"
quote_elements = soup.find_all('div', class_='quote')

# Liste for å lagre de strukturerte dataene
data = []

# Gå gjennom hvert quote-element og trekk ut ønsket data
for element in quote_elements:
    # Hent ut sitatets tekst
    text = element.find('span', class_='text').get_text()
    # Hent ut forfatterens navn
    author = element.find('small', class_='author').get_text()
    # Hent ut alle taggene tilknyttet sitatet
    tags = [tag.get_text() for tag in element.find_all('a', class_='tag')]
    
    # Legg dataen til i lista som en ordbok
    data.append({
        'text': text,
        'author': author,
        'tags': tags
    })

# Skriv ut den strukturerte dataen
for item in data:
    print(item)
