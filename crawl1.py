# -*- coding: utf-8 -*-
from threading import Thread
from bs4 import BeautifulSoup
import requests
import time
import os

#crawl duong
def findBestItem():
    parent_dir = "/home/nhh/dev/test"
    # for to MAX_PAGE
    # headers = {
    #     'User-Agent': 'Go to | https://www.whatismybrowser.com/detect/what-is-my-user-agent |, Get your User-Agent and paste here'}

    searchLinks = [
        "https://iwater.vn/ten-duong-sai-gon/danh-sach-nhung-ten-duong-o-quan-thu-duc-thanh-pho-ho-chi-minh-14288.html",
        "https://iwater.vn/ten-duong-sai-gon/danh-sach-nhung-ten-duong-o-quan-tan-binh-thanh-pho-ho-chi-minh-14957.html",
        "https://iwater.vn/ten-duong-sai-gon/danh-sach-nhung-ten-duong-o-quan-tan-phu-thanh-pho-ho-chi-minh-14289.html",
        'https://iwater.vn/ten-duong-sai-gon/danh-sach-nhung-ten-duong-o-quan-phu-nhuan-thanh-pho-ho-chi-minh-14291.html',
        "https://iwater.vn/ten-duong-sai-gon/danh-sach-nhung-ten-duong-o-quan-binh-thanh-thanh-pho-ho-chi-minh-14292.html",
        "https://iwater.vn/ten-duong-sai-gon/danh-sach-nhung-ten-duong-o-quan-go-vap-thanh-pho-ho-chi-minh-14293.html",
        "https://iwater.vn/ten-duong-sai-gon/danh-sach-nhung-ten-duong-o-quan-binh-tan-thanh-pho-ho-chi-minh-14294.html",
        "https://iwater.vn/ten-duong-sai-gon/danh-sach-nhung-ten-duong-o-huyen-binh-chanh-thanh-pho-ho-chi-minh-14295.html",
        "https://iwater.vn/ten-duong-sai-gon/danh-sach-nhung-ten-duong-o-huyen-can-gio-thanh-pho-ho-chi-minh-14296.html",
        "https://iwater.vn/ten-duong-sai-gon/danh-sach-nhung-ten-duong-o-huyen-cu-chi-thanh-pho-ho-chi-minh-14297.html",
        "https://iwater.vn/ten-duong-sai-gon/danh-sach-nhung-ten-duong-o-huyen-hoc-mon-thanh-pho-ho-chi-minh-14298.html",
        "https://iwater.vn/ten-duong-sai-gon/danh-sach-nhung-ten-duong-o-huyen-nha-be-thanh-pho-ho-chi-minh-14299.html"
    ]


    for searchLink in searchLinks:
        directory = searchLink[69:-33].replace("-"," ")
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)
        print(directory)

        # response = requests.get(searchLink, headers=headers)
        response = requests.get(searchLink)
        # response = requests.get(searchLink)


        bsoup = BeautifulSoup(response.text, "lxml")


        # <a> class = search-a-product-item
        # listElement = bsoup.findAll("ul", {"class": "links-container"})
        # listElement = bsoup.findAll("ul", {"class": "links-container"})
        path_street = os.path.join(path, "street.txt")
        path_ward = os.path.join(path, "ward.txt")
        f1 = open(path_ward, "w")
        f1.close()

        f = open(path_street, "w")
        # f.write(bsoup.find("ul", {"class": "links-container"}).text)
        # f.close()
        #
        # f2 = open("hotspot1.txt", "a")
        adlist = bsoup.findAll("td")
        for li in adlist:
            if li.text[0] == ' ':
                f.write(li.text[1:] + "\n")
            else:
                f.write(li.text + "\n")

            # link =  "https://moovitapp.com/index/vi/" + li.contents[0].attrs['href']
            # respon = requests.get(link)
            # bsoup = BeautifulSoup(respon.text, "lxml")
            # f1.write(bsoup.find("div", {"class": "search-field to"}).find("input").attrs['value'] + "\n")

            # list1 = bsoup.findAll("li", {"class": "route-container"})
            # for idx in list1:
                # f2.write(idx.find("h3").text[3:] + "\n")
        f.close()
        # f2.close()

findBestItem()

