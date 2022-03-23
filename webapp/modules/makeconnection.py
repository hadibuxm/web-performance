# Import required packages
import json
import requests
import pandas as pd
import urllib
import time
from google.colab import files
import io

# API request url
api_key = 'AIzaSyCU8rQoU5lZGiA1NRKmy5Ac-uyTR3PQeAw'

def fetch_metrics(url):
# make connection and fetch results
    fetch_results = urllib.request.urlopen('https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url='+url+'/&strategy=desktop&key='
                                +api_key\
                                    .format(url)).read().decode('UTF-8')
    # create json
    result_json = json.loads(fetch_results)
    return result_json


