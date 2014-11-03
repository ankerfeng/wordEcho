#/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@version: 1.0
@author: bkwy.org
'''
import Tkinter
import seek
from Tkinter import Frame, Entry, Message, Button
from Tkconstants import *
from textwrap import fill
from ttk import Scrollbar

#创建GUI
class Panle:
    def __init__(self, master):
        
        self.frame = Frame(master)
        self.frame.pack(side=TOP)
        self.label = Tkinter.Label(self.frame, text='wordEcho')
        self.label.pack()
        self.input = Entry(self.frame, width=45)
        self.input.pack(side=LEFT)
        self.button = Button(self.frame, text='翻译')
        self.button.pack(side=RIGHT)
        self.frame2 = Scrollbar(master)
        self.frame2.pack(side=TOP)
        self.ms = Message(self.frame2,  anchor='w', width=150)
        self.ms.pack()
        

if __name__ == '__main__':
    root = Tkinter.Tk()
    root.geometry('400x300')
    panle = Panle(root) 
    
    #事件处理，翻译输入的单词
    def find(event):
        str = panle.input.get()
        print str
        word = seek.translate(str)
        translist = ''
        i = 0
        while(i<len(word)):
            translist += word[i]+'\n'
            i += 1
        panle.ms.config(text=translist)
        
    #事件绑定
    panle.input.bind('<Return>', find)
    panle.button.bind('<Button-1>', find)
    Tkinter.mainloop()
    