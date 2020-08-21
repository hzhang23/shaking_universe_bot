import requests
from weibo import Client
import requests
import wget
import os
import datetime

apodurl = "https://api.nasa.gov/planetary/apod?api_key=XcZZaNTbWiVB9dfRLcesONOULtyTOG4gCahxwOG2&date=2017-02-22"
apodjson = requests.get(apodurl).json()
pictitle = apodjson.get("title")
picdate = apodjson.get("date")
picurl = apodjson.get("url")
picexp = apodjson.get("explanation")
today = datetime.datetime.now().date().strftime("%Y-%m-%d")


APP_KEY = "4180574602"
APP_SECRET = "6e1e5631435df560cb61ef979d7c20ae"
CALLBACK = "https://github.com/hzhang23/shaking_universe_bot"
USERNAME = "ikkiuniverse@gmail.com"
PASSWORD = "jbjhhzstsl1"

def share_NASApicoftheday(text, imgurl):
    out_file = "./"
    picoftheday = wget.download(imgurl, out=out_file)
    path = os.path.abspath(picoftheday)
    uploader = open(path, 'rb')
    c = Client(APP_KEY,APP_SECRET, CALLBACK, username=USERNAME,password=PASSWORD)
    c.post('statuses/share', status=text+ "http://www.baidu.com",pic=uploader)
    uploader.close()
    os.remove(path)

share_NASApicoftheday(pictitle, picurl)
# pict = open('download.jpeg','rb')
# c.post('statuses/share', status="周正龙"+ "http://www.baidu.com",pic=pict)
# pict.close()


