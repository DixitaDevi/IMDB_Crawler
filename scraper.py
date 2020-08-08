import requests
from csv import writer
from csv import reader
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


def scrape(max_pages):
    page = 1
    filename = "celebreties2.csv"
    f = open(filename, "w")
    headers = "IMAGE_LINKS, NAMES, DESCRIPTION, WIKI-LINK\n"
    f.write(headers)
    while page <= max_pages:
        my_url = 'https://www.imdb.com/list/ls068010962/?sort=list_order,asc&mode=detail&page=' + str(page)
        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()
    

        page_soup = soup(page_html, "html.parser")
        links = page_soup.findAll("div", {"class":"lister-item-image"})
        titles = page_soup.findAll("div", {"class":"lister-item-content"})


        for i in range(len(links)):
            try:
                link = links[i]
                image_source = link.a.img["src"]
                print(image_source)
                
                title = titles[i]
                name_source = title.a.string[:-1]
                print(name_source)

                per_trait = titles[i].findAll("p")
                desc = per_trait[1].text[1:].strip().replace('.','\n').replace('!', '\n')
                s1 = desc.strip().split("\n")[0].strip()
                s2 = desc.strip().split("\n")[1].strip()
                desc = s1+". "+s2
                print(desc)

                desc_link = 'https://en.m.wikipedia.org/wiki/'+name_source.strip().replace(' ', '_')
                print(desc_link)
                
                f.write(image_source.replace(",", "") +" , "+name_source+" , "+desc.replace(",", "")+" , "+desc_link.replace(",", "")+"\n")
            except:
                print("Exception caught")
        page += 1

scrape(2)


