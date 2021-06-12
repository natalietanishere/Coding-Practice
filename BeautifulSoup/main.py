from bs4 import BeautifulSoup 
import requests #getting access to websites
import csv #means comma-seperated values, great for organizing spreadsheets

URL = "http://www.values.com/inspirational-quotes"
quotes =[] 
req = requests.get(URL)
soup = BeautifulSoup(req.content, 'html5lib')

table = soup.find('div', attrs={'id':'all_quotes'}) #attrs means attributions
for i in table.findAll('div',attrs={'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'} ):
  quote = {}
  quote['theme'] = i.h5.text #quote text
  quote['url'] = i.a['href'] #accessing hyperlink
  quote['img'] = i.img['src'] #accessing image link
  quotes.append(quote)

  filename = 'export.csv'
  with open(filename,'w',newline='') as x: #w means writing
    write = csv.DictWriter(x,['theme','img','url']) #csv is organized into dicts
    write.writeheader()
    for quote in quotes:
      write.writerow(quote)
