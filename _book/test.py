#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

path = "/Users/limbo/github/stackoverflow_python/part1"
create_path = "/Users/limbo/github/stackoverflow_python/data"


def create_file(path, name, content):
    with open('{}/{}'.format(path, name), 'w') as F:
        F.write(content)

files= os.listdir(path)

for name in files:
    with open(path + "/" + name, "r") as F:
        pre_content = ""
        content = ""
        flag = 0
        for line in F.readlines():
            if line.startswith('***'):
                flag = 1

            if flag:
                content += line
            else:
                pre_content += line

        pid = re.search(r"http://stackoverflow.com/questions/(\d+)/", pre_content).group(1)
        name = pid + ".md"
        create_file(create_path, name, content)
