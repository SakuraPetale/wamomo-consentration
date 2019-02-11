#!/usr/bin/env python3
html_body = """
<html><body>
foo = %s
</body></html>
"""

import cgi

form = cgi.FieldStorage()
foo = form['foo'].value
print ("Content-type: text/html\n")
print (html_body %form.getvalue('foo', 'N/A'))

