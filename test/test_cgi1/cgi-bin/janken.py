# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import cgi
import random

form = cgi.FieldStorage()

dic = {"1": "グー", "2": "チョキ", "3": "パー"}

user = form.getfirst('janken')
user_choice = dic[user]

choice_list = ["1", "'2", "3"]
pc = dic[random.choice(choice_list)]

draw = '<font color="#32CD32">DRAW</font>'
win = '<font color="#FF7F50">You Win!!</font>'
lose = '<font color="#0000FF">You lose!!</font>'

if user_choice == pc:
  judge = draw
else:
  if user_choice == "グー":
    if pc == "チョキ":
      judge = win
    else:
      judge = lose

  elif user_choice == "チョキ":
    if pc == "パー":
      judge = win
    else:
      judge = lose

  else:
    if pc == u"グー":
      judge = win
    else:
      judge = lose


html_body = """
<html><body><center><br><br><br>
あなたが選んだのは %s<br><br>
コンピュータが選んだのは%s<br><br>
<font size="5">　結果は　%s </font><br><br>
<a Href ="http://0.0.0.0:8000/janken.html">戻る</a>
</center></body></html>""" % (user_choice, pc, judge)

print("Content-type: text/html\n")
print(html_body)

