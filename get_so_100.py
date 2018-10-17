#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re

from bs4 import BeautifulSoup
from lxml import etree
import datetime
import time

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

README_TEMPLETE = """
# Stackoverflow 上关于 Python 的问题
[![](https://img.shields.io/github/stars/taizilongxu/stackoverflow_python.svg?style=for-the-badge&label=Stars)](https://github.com/taizilongxu/stackoverflow_python) 

排名根据 vote 数量选取, 许多 SO 上的回答质量确实高, 有能力建议查看原文, 一般引用的文章也非常好,

翻译是根据 question id 写在 data 文件夹, 运行脚本 `get_so_100.py` 自动生成 `part` 部分文档

## 目录

> 图表数据更新时间 {}

| rank | vote | view | answer | url |中文|
|:-:|:-:|:-:|:-:|:-:|:-|
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

def make_readme(data):
    lines = []
    for index, i in enumerate(data):
        content = get_content_by_pid(i['pid'])
        file_name = '{}.md'.format(index + 1)
        cn_name = get_tran_title(content)
        line = "|{}|{}|{}|{}|[url](http://stackoverflow.com{})|[{}](part/{})|".format(index+1, i['vote'], i['views'],
                                        i['answers'], i['href'], cn_name, file_name)
        lines.append(line)

    update_time = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    return README_TEMPLETE.format(update_time, '\n'.join(lines))

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

def make_readme_file(data):
    with open('{}/README.md'.format(PATH), 'w') as F:
        F.write(data)

data = get_100()

content = make_summary(data)
make_summary_file(content)

readme = make_readme(data)
make_readme_file(readme)

make_question_files(data)
