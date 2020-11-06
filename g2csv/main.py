import json
import requests
from bs4 import BeautifulSoup


def main(event,context):
    response = []
    r = requests.get("https://www.google.com/search?q=" + event['keyword'])
    bs = BeautifulSoup(r.text, features="html.parser")
    for link in bs.find_all('div', {'class': 'g'}):
        title = link.find('a')
        url = link.find('cite')
        if title and url:
            response.append({'title':title.text,'url':url.text})
    return json.dumps(reponse,sort_keys=True, indent=4)


event = json.loads('{"Keyword"}:{"docker"}')
print(main(event,""))