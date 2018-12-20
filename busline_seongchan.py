import re
import urllib.request
import json
from selenium import webdriver
from bs4 import BeautifulSoup
from slackclient import SlackClient
from flask import Flask, request, make_response, render_template
import time


def busline(bus_num):
    # 웹사이트 열기
    driver = webdriver.Chrome(r'C:\Users\student\Desktop\chromedriver_win32\chromedriver.exe')
    url = "https://bus.gwangju.go.kr/busmap/lineSearch"
    driver.get(url)

    source = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(source, "html.parser")
    result = soup.find("div", class_="divSearch")
    # result = soup.find("div", id="contenttabledivGrid")
    # company = soup.find_all("div", class_="slide")
    # bt = driver.find_element_by_css_selector("button.btn.btn-default")  # 클래스만 있는경우
    # bt.click()
    result.get_text()
    time.sleep(1000)
    return

if __name__ == "__main__":

    busline(1)
    pass
