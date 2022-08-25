import requests
from datetime import datetime
from bs4 import BeautifulSoup
import random, string
from flask import Flask, jsonify, request, render_template
from time import time, sleep


app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


timetable = {}
tableNames = {}

quickTime = []
quick = []

stationNames = ["Piata 700", "Circumvalatiunii", "Mendeleev", "Hasdeu_1", "UTA_1", "Lapusneanul_1", "Alexandrescu_1", "Madona", "Taborului_2", "Razboieni", "Ciresului_2", "Rosseti", "Banul Severinului", "Grigore Ureche", "Rarau", "Ciocarliei", "IML", "IML", "Ciresului_1", "Razboieni", "Taborului_1", "Madona", "Alexandrescu_2", "Lapusneanul_2", "UTA_2", "Hasdeu_2", "Mendeleev", "Piata 700"]

def computeTimeTables(quickTime, quick):

  url = "http://86.125.113.218:61978/html/timpi/trasee.php?param1=2246"
  page = requests.get(url)
  
  soup = BeautifulSoup(page.content, "html.parser")

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
  comp_time = (realHour+3)*60 + realMin
  print(comp_time)
  print("====================")

  k = 0

  
  
  for child in soup.find_all('table'):
    for td in child.children:
      hour = 0
      minutes = 0
      timer = 0
      if(td.text != '\n'):
        if(td.text[-6] >= '0' and td.text[-6] <= '9'):
          #print(td.text[-6] + td.text[-5] + " " + td.text[-3] + td.text[-2])
          hour = int(td.text[-6])*10 + int(td.text[-5])
          minutes = int(td.text[-3])*10 + int(td.text[-2])
          timer = hour*60+minutes
          timetable[k] = abs(timer-comp_time), stationNames[k]
          #print(time)
          k = k+1
        elif td.text[-5] == 'm':
          timer = int(td.text[-7])
          #print(time)
          timetable[k] = timer, stationNames[k]
          k = k+1
          
          
         # tableNames[minutes] = stationNames[i]
          #print(stationNames[i])
  
  #print(rows)
  #print(timetable)
  
  
  
  for i in timetable:
    #print(timetable[i][0])
    #print(comp_time)
    #print(abs(timetable[i][0]-comp_time))
    #print("-----")
    quickTime.append(timetable[i][0])
    quickTime.append(timetable[i][1])
    quick.append(quickTime)
    quickTime = []
  
  #quick.sort()
  print(quick)
  
  #print(here/60)
  #print(hereMin)
  #print(hereStation)

computeTimeTables(quickTime, quick)

print ("starting...")
import threading

def printit():
  threading.Timer(5.0, printit).start()
  print ("Hello, World!")
  timetable.clear()
  quickTime.clear()
  quick.clear()
  computeTimeTables(quickTime, quick)

printit()

@app.route('/api', methods=['GET', 'POST'])  # What happens when the user visits the site
def data_get():
    if request.method == 'POST': # POST request
        print(request.get_text())  # parse as text
        return 'OK', 200
    
    else: # GET request
        return jsonify(quick)

@app.route('/')  # What happens when the user visits the site
def base_page():
	stationName = quick
	return render_template(
		'base.html',  # Template file path, starting from the templates folder. 
		station=stationName  # Sets the variable random_number in the template
	)

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
		port=random.randint(2000, 9000)  # Randomly select the port the machine hosts on.
	)
