import requests
from datetime import datetime
from bs4 import BeautifulSoup

now = datetime.now()
current_time = now.strftime("%H:%M")
print("====================")
print("Current time " + current_time)
realHour = 0

realHour = int(current_time[0])*10+int(current_time[1])
realMin = 0
realMin = int(current_time[3])*10+int(current_time[4])
print(realHour+3)
print(realMin)
print("====================")

url = "http://86.125.113.218:61978/html/timpi/trasee.php?param1=2246"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

rows = []
row = []

timetable = {}
tableNames = {}

stationNames = ["Piata 700", "Circumvalatiunii", "Mendeleev", "Hasdeu_1", "UTA_1", "Lapusneanul_1", "Alexandrescu_1", "Madona", "Taborului_2", "Razboieni", "Ciresului_2", "Rosseti", "Banul Severinului", "Grigore Ureche", "Rarau", "Ciocarliei", "IML", "IML", "Ciresului_1", "Razboieni", "Taborului_1", "Madona", "Alexandrescu_2", "Lapusneanul_2", "UTA_2", "Hasdeu_2", "Mendeleev", "Piata 700"]

for child in soup.find_all('table'):
  i = 0
  for td in child.children:
    hour = 0
    minutes = 0
    if(td.text != '\n'):
      if(td.text[-6] >= '0' and td.text[-6] <= '9'):
        row = []
        hour = int(td.text[-6])*10 + int(td.text[-5])
        minutes = int(td.text[-3])*10 + int(td.text[-2])
        row.append(hour)
        row.append(minutes)
        rows.append(row)
        i += 1
        timetable[minutes] = hour
        tableNames[minutes] = stationNames[i]
        print(stationNames[i])

print(rows)

here = 60
hereMin = 0
hereHour = 0

for i in timetable:
  
  #print(i)
  if(abs(i - realMin) < here):
    here = abs(i - realMin)
    hereMin = i

print(here)
print(hereMin)
print(stationNames[here])

