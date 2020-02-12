from bs4 import BeautifulSoup
import requests
import json

EVENT_DETAILS_PAGE = 'http://kirpalsagaracademy.com/4020000000.html'

response = requests.get(EVENT_DETAILS_PAGE)
soup = BeautifulSoup(response.text, 'html.parser')
raw_events = soup.select('.main-event-div')

events = [] # <1>

for raw_event in raw_events:
    ancestor_link = raw_event.parent.parent # <2>
    event = {
        "link": 'http://kirpalsagaracademy.com/' + ancestor_link['href'],
        "date": raw_event.select('.img-col span')[0].text,
        "title": raw_event.select('.events-name')[0].text
    }
    events.append(event)

print(json.dumps(events, indent=2)) # <3>
