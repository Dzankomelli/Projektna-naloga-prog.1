import json
import requests
import re
import tools
import page_saving

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
    r'\s+'
    r'<li>(.*)</li>' #data of first registration
    r'\s+'
    r'<li>(.*)</li><li>(.*)</li><li>(.*)</li>' #(1.) number of km, (2.) type of motor. (3.) type of transmission

)

cars = []
count = 1

for i in range(100, 101):
    content = tools.file_content(f'captured_data/{i}.page.html')
    print('----------------------NASLEDNJA STRAN--------------------')
    for match in re.findall(pattern, content):
        cars.append(match)
        print(match, count)
        count += 1

tools.write_json(cars, 'cars.json')        