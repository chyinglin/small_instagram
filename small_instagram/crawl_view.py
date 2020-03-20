from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from bs4 import BeautifulSoup
import requests


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
