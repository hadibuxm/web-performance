# Import required packages 
import json
import requests
import pandas as pd
import urllib
import time
from google.colab import files
import io 

# Define URL  
url = 'https://www.example.co.uk'

# API request url
result = urllib.request.urlopen('https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={}/&strategy=mobile'\
.format(url)).read().decode('UTF-8')

print(result)
