import json
import os
import re
import urllib.request

from bs4 import BeautifulSoup
from slackclient import SlackClient
from flask import Flask, request, make_response, render_template

def notification():
    url = "http://bus.gjcity.net/guide/notice/noticeList"
    source = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(source, "html.parser")

    # print(soup)
    subjects = []
    num = []
    # date=[]
    for subject in soup.find_all("a", class_="txt_pt13"):
        subjects.append(subject.get_text())
    for number in soup.find_all("td", class_="listtd txt_pt13"):
        num.append(number.get_text())
    return subjects



