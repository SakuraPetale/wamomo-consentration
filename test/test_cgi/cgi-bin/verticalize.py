#!/usr/bin/env python3
# coding: utf-8

import cgi

form=cgi.FieldStorage()
html_body = u"""
<html>
<head>
<meta http-equiv="content-type" content="text/html;charset=utf-8">
</head>
<body>
%s
</body>
</html>
"""

body_line=[]
body=form.getvalue('body', '')
# body=str(body, 'utf-8', 'ignore')
body = body
for cnt in range(0, len(body), 10):
    line=body[:10]
    line+=''.join([u'　' for i in range(len(line), 10)])
    body_line.append(line)
    body=body[10:]
body_line_v=[u''.join(reversed(x)) for x in zip(*body_line)]

print("Content-type: text/html\n")
print(html_body % '<br />'.join(body_line_v))
