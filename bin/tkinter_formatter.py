#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2016/09/22

@author: shohei
'''

from lib import space_formatter


def select_all(event):
    '''テキストウィジェット内のテキストを全選択する
    '''
    textWidget.tag_add(SEL, "1.0", END)
    textWidget.mark_set(INSERT, "1.0")
    textWidget.see(INSERT)
    return 'break'

def format_with_space(textWidget):
    u_content = unicode(textWidget.get("1.0", END))
    u_formatted_content = space_formatter.format_with_space(u_content)
    
    textWidget.delete("1.0", END)
    textWidget.insert(END, u_formatted_content)

if __name__ == '__main__':
    from Tkinter import Tk,Text,Button,mainloop,BOTH,YES,END,SEL,INSERT
    
    # ウィンドウ
    root = Tk()
    
    # textWidget
    textWidget = Text(root)
    textWidget.focus_set()
    textWidget.pack(fill=BOTH, expand=YES) # fillとexpandでウィンドウと一緒に大きさが変わるようにする。
    #textWidget.insert(END, "countrty   　capital    language\njapan       tokyo      日本語\n\namerica                english\n     \n\tEngland - english\n\tphilipenese  manila")
    textWidget.bind("<Control-Key-a>", select_all) # ctrl+aで全選択できるようにすうｒ
    
    # button
    button = Button(root, text = 'Format', command= lambda : format_with_space(textWidget))
    button.pack()
    
    mainloop()
