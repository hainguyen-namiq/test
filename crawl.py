# -*- coding: utf-8 -*-
from threading import Thread
from bs4 import BeautifulSoup
import requests
import time
import os

def findBestItem(page):



    # for to MAX_PAGE
    # headers = {
    #     'User-Agent': 'Go to | https://www.whatismybrowser.com/detect/what-is-my-user-agent |, Get your User-Agent and paste here'}



    searchLink = "https://moovitapp.com/index/vi/ph%C6%B0%C6%A1ng_ti%E1%BB%87n_c%C3%B4ng_c%E1%BB%99ng-streets-Th%C3%A0nh_ph%E1%BB%91_H%E1%BB%93_Ch%C3%AD_Minh-"+ str(page) +"-2880"
    # response = requests.get(searchLink, headers=headers)
    response = requests.get(searchLink)
    # response = requests.get(searchLink)

    if response.status_code != 200:
        return

    bsoup = BeautifulSoup(response.text, "lxml")




    # <a> class = search-a-product-item
    # listElement = bsoup.findAll("ul", {"class": "links-container"})
    listElement = bsoup.findAll("ul", {"class": "links-container"})

    f = open("street.txt", "a")
    f.write(bsoup.find("ul", {"class": "links-container"}).text)
    f.close()

    f1 = open("address.txt", "a")
    f2 = open("hotspot1.txt", "a")
    adlist = bsoup.findAll("ul", {"class": "links-container"})[0].findAll("li") #getlink thay i
    for li in adlist:
        time.sleep(0.1)
        link =  "https://moovitapp.com/index/vi/" + li.contents[0].attrs['href']
        respon = requests.get(link)
        bsoup = BeautifulSoup(respon.text, "lxml")
        f1.write(bsoup.find("div", {"class": "search-field to"}).find("input").attrs['value'] + "\n")

        list1 = bsoup.findAll("li", {"class": "route-container"})
        for idx in list1:
            f2.write(idx.find("h3").text[3:] + "\n")
    f1.close()
    f2.close()


for i in range(7,10):
    print(i)
    time.sleep(1)
    findBestItem(i)

