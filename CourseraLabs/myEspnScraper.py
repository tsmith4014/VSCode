import requests
from bs4 import BeautifulSoup



page = requests.get('https://www.espn.com/nfl/team/stats/_/name/buf/table/passing/sort/passingTouchdowns/dir/desc').text
#print(page)
soup = BeautifulSoup(page, 'html.parser')

artists = soup.find_all('a')

for artist in artists:
    names = artist.contents[0]
    fullLink = artist.get('href')
    print(names)
    print(fullLink)


