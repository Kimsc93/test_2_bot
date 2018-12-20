import json
import os
import re
import urllib.request

from bs4 import BeautifulSoup
from slackclient import SlackClient
from flask import Flask, request, make_response, render_template

def notification():
    text = re.sub(r'<@\S+> ', '', text)  # 아이디 떼는 코드
    url = "http://bus.gjcity.net/guide/notice/noticeList"
    source = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(source, "html.parser")
    company = soup.find_all("div", class_="slide")



