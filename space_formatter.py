#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2016/09/22

@author: shohei
'''
import unicodedata
import os

# 定数
NUM_OF_SPACE_BETWEEN_COLUMNS = 2 # 各列間の半角スペースの数

def ___get_word_width(u_word):
    '''unicode文字列の幅を数えて返す。
    
    例：アメリカは「8」。americaは「7」。
    '''
    width = 0
    for u_char in u_word:
        width += __get_char_width(u_char)
    return width

def __get_char_width(u_char):
    '''unicode文字の幅を返す。
    
    例：「あ」は「2」。「a」は「1」
    '''
    if 'NaH'.count(unicodedata.east_asian_width(u_char)) > 0:
        return 1 #半角
    else:
        return 2 #全角
    
def format_with_space(u_str):
    '''unicode文字列を整形して、整形後のunicode文字列を返す。
    '''
    if not isinstance(u_str, unicode):
        raise TypeError("argument is not of unicode type. It is " + str(type(u_str)))
    
    u_lines = u_str.splitlines()
    
    # calculate the max width of every column
    max_col_width_list = [] # each element has the max width of column.
    for u_line in u_lines:
        cols = u_line.strip().split()
        for col_i, u_col in enumerate(cols):
            col_width = ___get_word_width(u_col)
            if col_i >= len(max_col_width_list):
                max_col_width_list.append(0)
            if col_width > max_col_width_list[col_i]:
                max_col_width_list[col_i] = col_width
    
    # prep is done. from here on, real formatting happens.
    formatted_lines = [] # formatted text goes in here
    for u_line in u_lines: # go through every line again.
        cols = u_line.strip().split()
        formatted_line = u""
        for col_i, u_col in enumerate(cols):
            max_col_width = max_col_width_list[col_i]
            col_width = ___get_word_width(u_col)
            padding = u" " * (max_col_width - col_width)
            # format the column and append to the line.
            formatted_line = formatted_line + u_col + padding + u" " * NUM_OF_SPACE_BETWEEN_COLUMNS
        formatted_lines.append(formatted_line)
    
    #if os.name == "nt":
    #    nl = "\r\n"
    #else:
    #    nl = "\n"
    #return nl.join(formatted_lines)
    #
    # I used to write above, but it did not work on Windows.
    # Apparently "\r\n" is interpreted and converted into "\n\r\n"
    # when put onto tkinter textWidget. So I fixed it as below. Now it works.
    return "\n".join(formatted_lines)

if __name__ == '__main__':
    #print(format_with_space(1))
    print(format_with_space(u"countrty   　capital    language\njapan       tokyo      日本語\n\nアメリカ合衆国                english\n     \n\tEngland - english\n\tphilipenese  manila"))
