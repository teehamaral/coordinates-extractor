import re
import sys
import requests

from bs4 import BeautifulSoup

args = sys.argv

if len(args) < 2:
    raise Exception('You must to pass the location as argument. E.g. python init.py "See me on Google Maps! https://maps.app.goo.gl/EGYoGW0WmMDbtNkD2"')

location = sys.argv[1]

regex = r'(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)'
match = re.findall(regex, location)

if not match:
    raise Exception('No URL found.')
elif 'maps' not in match[0]:
    raise Exception('Google Maps URL not found. Try again.')

response = requests.get(match[0])
html_doc = response.content

soup = BeautifulSoup(html_doc, 'html.parser')
scripts = soup.head.find_all('script')
coordinates = None
for script in scripts:
    text = script.get_text()
    items = text.split(',')
    try:
        lat = '{lat}'.format(lat=items[2])
        lat = lat.replace('[', '').replace(']', '')
        long = '{long}'.format(long=items[1])
        long = long.replace('[', '').replace(']', '')
        coordinates = '{},{}'.format(lat, long)
    except Exception as e:
        print(e.args)

print ('%s: %s' % (match[0], coordinates))


