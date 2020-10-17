#Midterm
#some imports
import re
import urllib.request
import json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context #this help to lift the certification for that https
api_endpoint = "https://api.exchangerate-api.com/v4/latest/"

#decorator
def loggable(func):         
    def inner(arg1,arg2,arg3): #here are three parameters
        s = func(arg1,arg2,arg3)
        with open("log.txt", "a") as log_file:
            log_file.write("Input:{}\n".format(arg1,arg2,arg3))
            log_file.write("Output:{}\n".format(s))
        return s
    return inner #return the decorator function


def page_exists(page): #test if the api endpoint exits
    try:
        urllib.request.urlopen(page)
        return True
    except:
        return False

        