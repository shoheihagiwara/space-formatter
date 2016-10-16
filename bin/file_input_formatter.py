#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2016/09/22

@author: shohei
'''
import sys
import codecs
from lib import space_formatter

if __name__ == '__main__':
    
    # 引数受け取り。1番目はファイルパス。2番目はファイルのエンコーディング
    file_path = sys.argv[1]
    if len(sys.argv) > 2:
        file_enc = sys.argv[2]
    else:
        file_enc = "utf-8" # デフォルトはutf-8
    
    # ファイルから読み込み
    with codecs.open(file_path, encoding=file_enc) as file_in:
        u_str = unicode(file_in.read())
    
    # フォーマットを整える
    formatted_string = space_formatter.format_with_space(u_str)
    
    # 結果をファイルに書き込む。書き込む先は読み込んだファイルと同じ場所。ファイル名は末尾に「.out」をつけたものにする。
    with codecs.open(file_path + ".out", mode="w", encoding=file_enc) as file_out:
        file_out.write(formatted_string)
        