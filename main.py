import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from urllib import request
site = "https://ytmp3.cc/"
anaurl = "https://www.youtube.com/playlist?list=PL_5mTF6Dw_03VRs0ZGSB6akDzJhxPS-la" # playlist url
plistesi = []
def getPlaylist(url):  # getting playlist and storing every video link in a list /
    sourceCode = requests.get(url).text
    soup = BeautifulSoup(sourceCode, 'html.parser')
    domain = 'https://www.youtube.com'
    for link in soup.find_all("a", {"dir": "ltr"}): # to find all video links
        href = link.get('href')
        if href.startswith('/watch?'):
            strtemp = domain + href
            plistesi.append(strtemp)


def indir(url):
    sleep(2)
    box1 = br.find_element_by_id("input")
    box1.send_keys(url)
    box1.submit()
    sleep(3)
    btn1 = br.find_element_by_id("download")
    dosya = str(btn1.get_attribute("href"))
    title1 = br.find_element_by_id("title").text
    print(title1+" dosyasi indiriliyor......")
    title1 = title1+".mp3"
    request.urlretrieve(dosya,title1)
    sleep(5)
    print("{} dosyasi kaydedildi...".format(title1))
    btn2 = br.find_element_by_link_text("Convert next")
    btn2.click()

getPlaylist(anaurl) # get playlist
if(plistesi):      # if playlist is not empty then you can start to download
    br = webdriver.Firefox()  # you should install selenium and webdriver for me it is mozilla geckodriver
    br.get(site)
    for i in range(len(plistesi)):
        indir(plistesi[i])
    br.close()
else:
    print("hata.......")


