#!/usr/bin/env python
# -*- coding:utf-8 -*-
#write by Qiaoy<traceurq@gmail.com>
#小凤直播室录音下载小脚本

import urllib2,re

site1 = "http://www.sdgb.cn/cms/html/video/jingjipindao/xiaofeng/index.html"
site2 = "http://www.sdgb.cn/cms/html/video/jingjipindao/xiaofeng/list_600_2.html"
site3 = "http://www.sdgb.cn/cms/html/video/jingjipindao/xiaofeng/list_600_3.html"
real = {}
title = []
real_mp3 = []

def find_real(site):
    value = urllib2.urlopen(site).read()
    tmppage = re.findall(r'<a href=\'(/cms/.*?)\'',value)
    for i in tmppage:
        page = "http://www.sdgb.cn"+i
        new_value = urllib2.urlopen(page).read()
        title.append(re.findall(r'<link rel=\"alternate\" type=\"application/rss\+xml\" title=\"(.*?)\"',new_value)[0])
        mp3 = re.findall(r'myajax.SendGet2\(\"(/cms/plus/play.php.*?)\"',new_value)
        for j in mp3:
            new_page = "http://www.sdgb.cn"+j
            real_mp3_page = urllib2.urlopen(new_page).read()
            real_mp3.append(re.findall(r'<param name=\"url\" value=\"(.*?)\"',real_mp3_page)[0])
        for x in xrange(len(title)):
            real[title[x]] = real_mp3[x]

find_real(site1)
find_real(site2)
find_real(site3)

for key in real:
    print "%s ---> %s"%(key,real[key])
