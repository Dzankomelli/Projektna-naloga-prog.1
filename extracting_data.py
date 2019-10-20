import json
import requests
import re
import tools



pattern = (
    r'<!--------------------- DESCRIPTION  ------------------->'
    r'\s+'
    r'<a class=".*" href=".*">'
    r'\s+'
    r'<span>(.*)</span>' #exctrating car name and model
    r'\s+'
    r'</a>'
    r'\s+'
    r'<!--------------------- DATA  ------------------->'
    r'\s+'
    r'<ul>'
    r'<li>(.*)</li>' #data of first registration
    r'\s+'
    r'<li>(.*)</li><li>(.*)</li><li>(.*)</li>' #(1.) number of km, (2.) type of motor. (3.) type of transmission

)

cars = []
count = 0

content = file_content('1.page.html')
for i in re.finditer(pattern, content):
    cars.append(pattern.groupdict())
    count += 1
print(count)