import requests
from bs4 import BeautifulSoup
def trusted(command):
    URL = "https://www.google.com/search?q=" + command
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    answer=soup.find('div',attrs={'class': "BNeawe iBp4i AP7Wnd"})
    return answer
def untrusted(command):
    URL = "https://www.google.com/search?q=" + command
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    uu = soup.find('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'}).text
    x = uu.split(' ')
    y = []
    for i in x:
        if '...' in i:
            break
        else:
            y.append(i)

    return(' '.join(y))
def main():
    query=input('Please Enter What you want to search here : ')
    print('By Google It Self : ' , trusted(query).text) # it is the content by google it self like what is weather ETC
    print('By the Website Which Rank On top : ' , untrusted(query))
main()

