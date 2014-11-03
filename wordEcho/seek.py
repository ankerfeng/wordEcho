#/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@version: 1.0

@author: bkwy.org
'''
import re
import urllib2
import thread
from urllib import urlopen

#读取本地原有单词本
def readldic():
    try:
        f = open('oxfordc.txt', 'r')
        dic = f.read()
        f.close()
        return dic
    except Exception, e:
        print e
#读取用户更新的单词本
def readselfdic():
    try:
        f2 = open('localselfdic.txt', 'r')
        selfdic = f2.read()
        f2.close()
        print selfdic
        return selfdic
        
    except Exception, e:
        print e
    
#添加陌生的单词
def localaddd(keyword, trans):
    f = open('localselfdic.txt', 'a')
    i = 0
    str = keyword+' '
    while(i<len(trans)):
        str += trans[i] + ';'
        i += 1
    str += '\n'
    f.write(str)
    f.close()
    
#解析网页
def filter(http, str):   
    http = http.replace('\n', '')
    http = http.replace(' ', '')
    par = '<divclass="group_pos">.*<divclass="net_paraphrase">'
    par = re.compile(par)
    word = par.findall(http)
    #print word[0]
    try:
        str = word[0]
    except Exception, e:
        print e
        word = ["No such word!"]
        
    par = re.compile('<label>.*?</label>')
    if word is not None:
        word = par.findall(str)
    
    i=0
    while(i<len(word)):
        word[i] = word[i].replace('<label>', '')
        word[i] = word[i].replace('</label>', '')
        #print word[i]
        i+=1
    return word
    
#远程查找
def remotedic(str):  
    url = "http://www.iciba.com/" + str
    try:
        req = urllib2.urlopen(url)
        http = req.read()
        word = filter(http, str)
        localaddd(str, word)
        return word
    except Exception, e:
        print e
        
    return ["remote feild!"]
    #print word

#本地查找
def local(str, dic):
    par = str+' .*'
    par = re.compile(par)
    word = par.findall(dic)
    if word:
        #return word
        #i = 0
        #while(i<len(word)):
            #print word[i]
            #i += 1
        i = 0
        while(i<len(word)):
            word[i] = word[i].replace(";", "\n")
            i += 1
        return word

    
#翻译
def translate(str):  
    word = local(str, readldic())
    if word is not None:
        return word
    else:
        word = local(str, readselfdic())
        if word is not None:
            return word
        else:
            print 'remote'
            return remotedic(str)
    
    
if __name__ == '__main__':

    while(True):
        str = raw_input('>')
        word = translate(str)
        i = 0
        while (i < len(word)):
            print word[i]
            i += 1
    