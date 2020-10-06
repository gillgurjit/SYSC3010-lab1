import random
import urllib.request
import requests
import threading

def thingspeak():
    
    val1 = 'gurjitgill@cmail.carleton.ca'
    val2 = 'L2-M-6'
    val3 = 'b'
    
    URL = 'https://api.thingspeak.com/update?api_key='
    KEY = '54CDA6FJF4RCJ92C'
    HEADER = '&field1={}&field2+{}&field3={}'.format(val1,val2, val3)
    new_URL = URL + KEY + HEADER
    print(new_URL)
    data = urllib.request.urlopen(new_URL)
    print(data)
    
if __name__== "__main__":
    
    thingspeak()
