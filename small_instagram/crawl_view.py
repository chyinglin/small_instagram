from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from bs4 import BeautifulSoup
import requests
import re
import urllib


def crawl(request):
    return render(request, 'crawl.html')


def post_crawl(request):
    url = request.POST["title"]
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    post = []
    h_tag = soup.find_all('h2')
    for h in h_tag:
        post.append(h.text)

    return render(request, 'crawl_result.html', locals())


def crawl_news(request):
    url = 'https://tw.appledaily.com/new/realtime'
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15'  # 偽裝使用者
    headers = {'User-Agent': user_agent}
    data_response = urllib.request.Request(url=url, headers=headers)
    data = urllib.request.urlopen(data_response)
    data = data.read().decode('utf-8')
    sp = BeautifulSoup(data, "html.parser")

    date = ""
    date = sp.find("h1", {"class": "dddd"})

    news_block = sp.find("ul", {"class": "rtddd slvl"})

    time_list = []
    times = news_block.findAll("time")
    for time in times:
        time_list.append(time.text)

    category_list = []
    categorys = news_block.findAll("h2")
    for category in categorys:
        category_list.append(category.text)

    title_list = []
    titles = news_block.findAll("h1")
    for title in titles:
        title_list.append(title.text)

    link_list = []
    links = news_block.findAll("a", href=re.compile('appledaily'))
    for link in links:
        link_list.append(link['href'])

    all = zip(time_list, category_list, title_list, link_list)
    return render(request, "crawl_news.html", locals())
