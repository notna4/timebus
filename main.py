import requests
from bs4 import BeautifulSoup

url = "http://86.125.113.218:61978/html/timpi/trasee.php?param1=2246"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

rows = []
row = []

for child in soup.find_all('table'):
  for td in child.children:
    yes = 0
    if(td.text != '\n'):
      print(td.text)

      for i in range(0, len(td.text)):
        if(td.text[i] == "\n"):

          if(td.text[i-1].isalpha()):
            print("acum: " + td.text[i-1])

print(rows)