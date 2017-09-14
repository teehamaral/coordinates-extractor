import re
import sys
import requests

from bs4 import BeautifulSoup

class CoordinatesExtractor(object):

    def __init__(self, text, *args, **kwargs):
        self.text = text
        self.lat = None
        self.long = None
        self.regex = r'(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)'

    def text_check(self):
        match = re.findall(self.regex, self.text)
        return True if match and 'maps' in match[0] else False

    def get_match(self):
        match = re.findall(self.regex, self.text)

        if not match:
            raise Exception('No URL found.')
        elif 'maps' not in match[0]:
            raise Exception('Google Maps URL not found. Try again.')
        else:
            return match[0]

    def get_coordinates(self):
        response = requests.get(self.get_match(), timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        scripts = soup.head.find_all('script')
        
        for tag in script_tags:
            text = tag.get_text()
            items = text.split(',')
            try:
                lat = '{lat}'.format(lat=items[2])
                self.lat = float(lat.replace('[', '').replace(']', ''))
                long = '{long}'.format(long=items[1])
                self.long = float(long.replace('[', '').replace(']', ''))                
            except:
                pass

            break
        
        return self.lat, self.long