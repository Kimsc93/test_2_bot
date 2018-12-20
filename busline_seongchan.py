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