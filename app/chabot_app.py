# -*- coding: utf-8 -*-
import json
import os
import re
import urllib.request

from bs4 import BeautifulSoup
from slackclient import SlackClient
from flask import Flask, request, make_response, render_template

app = Flask(__name__)

slack_token = "xoxb-502761537154-508544948647-Gk3fNaEt2nmyLhTAL1Zt8P7T"
slack_client_id = "502761537154.506753527072"
slack_client_secret = "f6c1a9a5028b8d226971fdd12fbae2b1"
slack_verification = "5LgIeKMidAPINmXXl0eJiiir"
sc = SlackClient(slack_token)

# 크롤링 함수 구현하기
def _crawl_naver_keywords(text):
    text = re.sub(r'<@\S+> ', '', text) #아이디 떼는 코드
    url = "http://www.jobkorea.co.kr/Salary/"
    source = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(source, "html.parser")
    company = soup.find_all("div", class_="slide")

    i = 0

    if "대기업" in text:
        i = 0
    elif "중견기업" in text:
        i = 1
    elif "공기업" in text:
        i = 2
    else:
        return u'it is not valid url.'

    result = company[i].get_text()[:-10].replace("\n\n\n\n", "\n").replace("\n\n", "\n").replace("\n\n", " ")

    return result


def _event_handler(event_type, slack_event):
    print(slack_event["event"])

    if event_type == "app_mention":
        channel = slack_event["event"]["channel"]
        text = slack_event["event"]["text"]

        keywords = _crawl_naver_keywords(text)
        sc.api_call(
            "chat.postMessage",
            channel=channel,
            text=keywords
        )

        return make_response("App mention message has been sent", 200, )

    # ============= Event Type Not Found! ============= #
    # If the event_type does not have a handler
    message = "You have not added an event handler for the %s" % event_type
    # Return a helpful error message
    return make_response(message, 200, {"X-Slack-No-Retry": 1})


@app.route("/listening", methods=["GET", "POST"])
def hears():
    slack_event = json.loads(request.data)

    if "challenge" in slack_event:
        return make_response(slack_event["challenge"], 200, {"content_type":
                                                                 "application/json"
                                                             })

    if slack_verification != slack_event.get("token"):
        message = "Invalid Slack verification token: %s" % (slack_event["token"])
        make_response(message, 403, {"X-Slack-No-Retry": 1})

    if "event" in slack_event:
        event_type = slack_event["event"]["type"]
        return _event_handler(event_type, slack_event)

    # If our bot hears things that are not events we've subscribed to,
    # send a quirky but helpful error response
    return make_response("[NO EVENT IN SLACK REQUEST] These are not the droids\
                         you're looking for.", 404, {"X-Slack-No-Retry": 1})


@app.route("/", methods=["GET"])
def index():
    return "<h1>Server is ready.</h1>"


if __name__ == '__main__':
    app.run('127.0.0.1', port=5000)
