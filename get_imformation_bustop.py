import re
import urllib.request
import json
from selenium import webdriver
from bs4 import BeautifulSoup
from slackclient import SlackClient
from flask import Flask, request, make_response, render_template
import time
import requests


def get_bus_stop_code(bus_stop):
    # 웹사이트 열기
    driver = webdriver.Chrome(r'./chromedriver.exe')
    url = "https://bus.gwangju.go.kr/busmap/stationSearch"
    driver.get(url)
    driver.find_element_by_id("BUSSTOP_NAME").send_keys(bus_stop)
    driver.find_element_by_id("btnBusStopSearch").click()

    div_table = driver.find_element_by_id("contenttabledivStationGrid")

    html = driver.page_source

    print(len(div_table.text))

    soup = BeautifulSoup(html, "html.parser")
    div_table = soup.find("div", id="contenttabledivStationGrid")
    div_row = div_table.find("div")


    for row in div_table:
        print(row.get_text())




if __name__=="__main__":
    bus_stop = '정광고'
    way = 0
    print(get_bus_stop_code(bus_stop))
    pass
