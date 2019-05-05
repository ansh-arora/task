import urllib.request
from bs4 import BeautifulSoup as soup

url='https://www.commonfloor.com/listing-search?city=Noida&search_intent=sale&polygon=1&page=1&page_size=30'

webpage=urllib.request.urlopen(url)
page_html=webpage.read()
webpage.close()
page_soup= soup(page_html, "html.parser")

props=page_soup.find_all('div',attrs={'class':'snb-tile'})


file='prop_list.csv'
f=open(file,"w")
headers="Property_title,Address,Price,Area\n"
f.write(headers)
for prop in props:
    t=prop.find_all('div',attrs={'class':'st_title'})
    title=t[0].h2.text

    ad=prop.find_all('a',attrs={'class':['gtpnd','gtloc']})
    b = []
    for a in ad:
        b.append(a.text)
    address= "|".join(b)

    pr=prop.find_all('span',attrs={'class':'s_p'})
    price=((pr[0].text).strip())

    ar=prop.find_all('div',attrs={'class':'infodata'})
    area=((ar[0].text).replace('\n',''))

    # print(title,'\n',address,'\n',price,'\n',area,'\n\n')
    f.write(title +","+ address +","+ price +","+ area +"\n")
f.close()
