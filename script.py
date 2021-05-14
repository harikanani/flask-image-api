import bs4
import requests
import shutil
import os
from datetime import datetime

GOOGLE_IMAGE = \
    'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'


def extract(data, quantity):
    URL_input = GOOGLE_IMAGE + 'q=' + data
    print('Fetching from url =', URL_input)
    URLdata = requests.get(URL_input)
    soup = bs4.BeautifulSoup(URLdata.text, "html.parser")
    ImgTags = soup.find_all('img')
    i=0
    # with open('fetch.txt',mode='r') as f:
    #     i = int(f.readline())

    print('Please wait..')
    while i < quantity:

        for link in ImgTags:
            try:
                images = link.get('src')
                ext = images[images.rindex('.'):]
                if ext.startswith('.png'):
                    ext = '.png'
                elif ext.startswith('.jpg'):
                    ext = '.jpg'
                elif ext.startswith('.jfif'):
                    ext = '.jfif'
                elif ext.startswith('.com'):
                    ext = '.jpg'
                elif ext.startswith('.svg'):
                    ext = '.svg'
                data = requests.get(images, stream=True)
                timestamp = datetime.timestamp(datetime.now())
                filename = str(timestamp) + ext
                # filename = str(i) + ext
                with open("static/img/"+filename, 'wb') as file:
                    shutil.copyfileobj(data.raw, file)
                i += 1
                # with open('fetch.txt','w') as f:
                #     f.write(str(i))
            except:
                pass
    print('\t\t\t Downloaded Successfully..\t\t ')


data = input('What are you looking for? ')
quantity = int(input('How many photos you want? '))
extract(data, quantity)
