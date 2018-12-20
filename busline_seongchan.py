import re
import urllib.request
import json
from selenium import webdriver
from bs4 import BeautifulSoup
from slackclient import SlackClient
from flask import Flask, request, make_response, render_template

driver = webdriver.Chrome(r'C:\Users\student\Desktop\chromedriver_win32\chromedriver.exe')

def busline(text):
    # 웹사이트 열기
    driver.get("https://bus.gwangju.go.kr/busmap/lineSearch")
    bt = driver.find_element_by_css_selector("button.btn.btn-default")  # 클래스만 있는경우
    bt.click()

    url = "http://www.jobkorea.co.kr/Salary/"
    source = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(source, "html.parser")
    company = soup.find_all("div", class_="slide")

    result = company[i].get_text()[:-10].replace("\n\n\n\n", "\n").replace("\n\n", "\n").replace("\n\n", " ")

    return result