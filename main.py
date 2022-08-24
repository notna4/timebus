import requests
from datetime import datetime
from bs4 import BeautifulSoup

now = datetime.now()
current_time = now.strftime("%H:%M")
print("====================")
print("Current time " + current_time)

comp_time = 0

realHour = 0

realHour = int(current_time[0])*10+int(current_time[1])
if(realHour+3 == 24):
  realHour = 0
realMin = 0
realMin = int(current_time[3])*10+int(current_time[4])
print(realHour+3)
print(realMin)
comp_time = realHour*60 + realMin
print(comp_time)
print("====================")

url = "http://86.125.113.218:61978/html/timpi/trasee.php?param1=2246"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

rows = []
row = []

timetable = {}
tableNames = {}

stationNames = ["Piata 700", "Circumvalatiunii", "Mendeleev", "Hasdeu_1", "UTA_1", "Lapusneanul_1", "Alexandrescu_1", "Madona", "Taborului_2", "Razboieni", "Ciresului_2", "Rosseti", "Banul Severinului", "Grigore Ureche", "Rarau", "Ciocarliei", "IML", "IML", "Ciresului_1", "Razboieni", "Taborului_1", "Madona", "Alexandrescu_2", "Lapusneanul_2", "UTA_2", "Hasdeu_2", "Mendeleev", "Piata 700"]

k = 0

for child in soup.find_all('table'):
  for td in child.children:
    hour = 0
    minutes = 0
    time = 0
    if(td.text != '\n'):
      if(td.text[-6] >= '0' and td.text[-6] <= '9'):
        hour = int(td.text[-6])*10 + int(td.text[-5])
        minutes = int(td.text[-3])*10 + int(td.text[-2])
        time = hour*60+minutes
        timetable[k] = time, stationNames[k]
        k = k+1
       # tableNames[minutes] = stationNames[i]
        #print(stationNames[i])

#print(rows)
print(timetable)

here = 24*60
hereMin = 0
hereHour = 0
hereStation = ""

for i in timetable:
  
  #print(timetable[i][2])
  if(abs(timetable[i][0] - comp_time) < here):
    here = abs(timetable[i][0] - comp_time)
    hereMin = timetable[i][0]
    hereStation = timetable[i][1]

print(here)
print(hereMin)
print(hereStation)

