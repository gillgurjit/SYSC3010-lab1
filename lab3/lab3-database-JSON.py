from urllib.request import * 
from urllib.parse import * 
import json
import sqlite3

# The URL that is formatted: http://api.openweathermap.org/data/2.5/weather?APPID=a808bbf30202728efca23e099a4eecc7&units=imperial&q=ottawa

# As of October 2015, you need an API key.
# I have registered under my Carleton email.
apiKey = "a808bbf30202728efca23e099a4eecc7";

# Query the user for a city
city = input("Enter the name of a city whose weather you want: ");

# Build the URL parameters
params = {"q":city, "units":"imperial", "APPID":apiKey };
arguments = urlencode(params);

# Get the weather information
address = "http://api.openweathermap.org/data/2.5/weather";
url = address + "?" + arguments;

webData = urlopen(url);
results = webData.read().decode('utf-8');
# results is a JSON string
webData.close();

#Convert the json result to a dictionary
# See http://openweathermap.org/current#current_JSON for the API

data = json.loads(results);

#Print the results

current = data["wind"];

dbconnect = sqlite3.connect("mydatabase.db");

dbconnect.row_factory = sqlite3.Row;

cursor = dbconnect.cursor();

cursor.execute('''CREATE TABLE IF NOT EXISTS weather (City text, Wind Speed NUMERIC)''');
cursor.execute('''insert into weather values (?, ?)''', [city, current["speed"]]);

dbconnect.commit();

cursor.execute('SELECT * FROM weather');

for row in cursor:
    print (row['City'], row['Wind Speed']);

dbconnect.close();

