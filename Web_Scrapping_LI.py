# created: 12/2/2021
# python 3.10
# sublime text 4

# status:  IN PROGRESS

import os
import numpy


# pip install beautifulsoup in cmd prompt
# pip install requests in cmd prompt
# otherwise will get error: "ImportError: No module named requests)"
import requests
from bs4 import BeautifulSoup



print( os.getcwd() )


url = 'https://www.linkedin.com/mynetwork/invite-connect/connections/'


request = requests.get(url)

print(request.status_code) 

# code 200 is good

print(request.text)