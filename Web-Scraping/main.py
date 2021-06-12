from bs4 import BeautifulSoup 
import requests #getting access to websites
import webbrowser #obtains the text for info

wiki_link = 'https://en.wikipedia.org/wiki/Special:Random'#website link
req = requests.get(wiki_link)

while True:
  soup = BeautifulSoup(req.content,'html.parser')
  #parser "beautifies", or analyzes data
  #xml files don't have classes, but html files do
  title = soup.find(class_='firstHeading').text
  print('Do you want to see the title page,' + title)
  ans = str(input('yes/no: '))
  if (ans.lower() == 'y'):
    url = 'https://en.wikipedia.org/wiki/%s' %title 
    #blank link
    webbrowser.open(url)#accessing url
    break
  else:
    print("Ok")
    break