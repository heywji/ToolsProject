#!/usr/bin/env python3
import bs4,requests
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36","Cookie":"laravel_session=eyJpdiI6IitocmhXTUhMcDJZeG9jK0ZTeW91bVE9PSIsInZhbHVlIjoiZXZXT0x4VURwRHpRYW9wdSt0TTRBTU5PUlU2elEwK2V4UGdDSmhJK2JyOEgwcDNKU0hoWnhhNE5rSEVGQThjbkRoeGwrc3VMcjNjM2FnQWtueDFIU0E9PSIsIm1hYyI6ImQxMWIxYTZjZjk4M2IxZjRjMzlkYmRiZGE0YzQyOGUxM2E0ZDJkZDdjMDU1NmMxMTAzZmE2OGEzZjMzMDgzNGQifQ%3D%3D"}

def file():
    with open('./download.txt') as f:
        for line in f:
            return f.readlines() 

# fread = file()
for fread in file():
     response = requests.get(url=fread,headers=headers)
     response.encoding = "utf-8"
     soup = bs4.BeautifulSoup(response.text,"lxml")
     list = soup.select("body > div > div > div.playground_wrap.area > ul > li > a")
     for i in list:
         print(i.get("href"))
