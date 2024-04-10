# coding=utf-8

import glob
import re

PATH = r"docs\*.md"

files = glob.glob(PATH)

def proc_toc():
    FILE = r"docs\README.md"

    PATTERN = r"- \[(.+?)\]\((.+?)\)"
    with open(FILE) as f:
        for s in f:
            m = re.match(PATTERN, s)
            if m:
                # print(m.groups())
                print("  - '%s': %s" % (m.group(1), m.group(2)))

def proc_file(f):
    
    with open(f, 'r') as file:
        # 读取文件内容
        content = file.readlines()

# 替换字符串
    if content[0].startswith("[") or content[0].startswith("Previous"):
        content[:] = content[1:]

    for i, s in enumerate(content):
        if s.find('src="images') > -1:
            content[i] = s.replace('src="images', 'src="../images')

    #content = content.replace('src="images', 'src="/images')

# 写回文件
    with open(f, 'w') as file:
        file.writelines(content)

proc_toc()
for f in files:
    #print(f)
    proc_file(f)

