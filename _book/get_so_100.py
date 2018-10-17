#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re

from bs4 import BeautifulSoup
from lxml import etree

URL = "https://stackoverflow.com/questions/tagged/python?page={}&sort=votes&pagesize=15"
PATH = "/Users/limbo/github/stackoverflow_python"

TEMPLETE = """
| rank | vote | view | answer | url |
|:-:|:-:|:-:|:-:|:-:|
|{index}|{vote}|{views}|{answers}| [url](http://stackoverflow.com{href}) |
"""

SUMMARY_TEMPLETE = """
# Summary

## 简介

* [Introduction](README.md)

## TOP 100

{}
"""


def get_page(num):
    data = []
    r = requests.get(URL.format(num))
    selector = etree.HTML(r.text)
    votes = selector.xpath('//*[@id="questions"]/div/div[1]/div[1]/div[1]/div/span/strong/text()')
    views = selector.xpath('//*[@id="questions"]/div/div[1]/div[2]/@title')
    titles = selector.xpath('//*[@id="questions"]/div/div[2]/h3/a/text()')
    hrefs = selector.xpath('//*[@id="questions"]/div/div[2]/h3/a/@href')
    answers = selector.xpath('//*[@id="questions"]/div/div[1]/div[1]/div[2]/strong/text()')

    for vote, view, title, href, answers in zip(votes, views, titles, hrefs, answers):
        data.append({
            'vote': vote,
            'views': get_view(view),
            'title': title,
            'href': href,
            'answers': answers,
            'pid': get_id(href)
        })

    return data

def get_view(view):
    return ''.join(view.split(','))[:-6]


def get_id(href):
    return href.split('/')[2]


def get_100():
    return get_page(1) + get_page(2)


def get_content_by_pid(pid):
    try:
        with open('{}/data/{}.md'.format(PATH, pid), 'r') as F:
            return ''.join(F.readlines())
    except Exception as e:
        return ''

def get_tran_title(content):
    try:
        title = re.search(r"## (.*?)\n", content).group(1)
        return title
    except Exception as e:
        return ''


def make_toc(trans_title, file_name):
    return "* [{}](part/{})".format(trans_title, file_name)


def make_summary(data):
    tocs = []
    for index, i in enumerate(data):
        content = get_content_by_pid(i['pid'])
        file_name = '{}.md'.format(index + 1)

        tocs.append(make_toc(get_tran_title(content), file_name))

    return SUMMARY_TEMPLETE.format('\n'.join(tocs))


def make_summary_file(content):
    with open('{}/SUMMARY.md'.format(PATH), 'w') as F:
        F.write(content)


def make_question_file(content, file_name):
    with open('{}/part/{}'.format(PATH, file_name), 'w') as F:
        F.write(content)


def make_question_files(data):
    for index, i in enumerate(data):
        i['index'] = index + 1
        content = get_content_by_pid(i['pid'])
        content = TEMPLETE.format(**i) + content
        file_name = '{}.md'.format(index + 1)

        make_question_file(content, file_name)

data = get_100()


content = make_summary(data)
make_summary_file(content)

make_question_files(data)
