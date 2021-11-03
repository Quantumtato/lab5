#!/usr/bin/python37all
import cgi
import json
data = cgi.FieldStorage()
s1 = data.getvalue('angle')
s2 = data.getvalue('home')
imput = {"angle":s1,"home":s2}

with open('lab5.txt', 'w') as f:
  json.dump(imput,f)

print('Content-type: text/html\n\n')

print("""
<html>
<form action="/cgi-bin/stepper_control.cgi" method="POST">
        <br>
        <input type="hidden" name="home" value="1">
        <input type="submit" value="Click to Home">
""")
print('<br> <br>')
print('<input type="range" name="angle" min ="0" max="360" value ="%s"><br>' %s1)
print("""<input type="submit" value="Change Angle">
</form>
</html>
""")