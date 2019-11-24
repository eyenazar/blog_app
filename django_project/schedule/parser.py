import requests
from bs4 import BeautifulSoup as bs

headers = {
    'accept': '*/*',
    'user-agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'
}

#base_url = 'http://schedule.iitu.kz/#/g/timetable/group/142941'
base_url = 'https://almaty.hh.kz/search/vacancy?area=160&st=searchVacancy&text=python'

def schedule_parse(base_url, headers):
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'lxml')
        div = soup.find_all('div', attrs={'id': 'app'})
        print(soup)                                                                                                             
    else:
        print('ERROR')

schedule_parse(base_url, headers)