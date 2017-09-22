import re
import sys
import requests
import vobject

from urllib import parse
from bs4 import BeautifulSoup

class CoordinatesExtractor(object):

    def __init__(self, text=None, file_path=None, *args, **kwargs):
        assert text or file_path, 'text or file_path are required'
        self.text = text
        self.lat = None
        self.long = None
        self.file_path = file_path
        self.regex = r'(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)'

    def get_coordinates_from_file(self):
        try:
            with open(self.file_path, 'r') as f:
                file_as_str = f.read()
                
            file_card = vobject.readOne(file_as_str)
            if hasattr(file_card, 'contents'):
                content = file_card.contents
                url = content.get('url', None)
                if url:
                    parse_url = parse.urlparse(url[0].value)
                    parse_query = parse.parse_qs(parse_url.query)
                    coordinates = parse_query.get('ll')
                    self.lat, self.long = coordinates[0].split(',')
        except Exception as e:
            print('Error: %s' % e.args)

        return self.lat, self.long

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
        script_tags = soup.head.find_all('script')
        
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