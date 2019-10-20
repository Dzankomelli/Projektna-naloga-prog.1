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
    r'<span>(?P<name_and_model>.*)</span>' #exctrating car name and model
    r'\s+'
    r'</a>'
    r'\s+'
    r'<!--------------------- DATA  ------------------->'
    r'\s+'
    r'<ul>'
    r'\s+'
    r'<li>(?P<registration>.*)</li>' #data of first registration
    r'\s+'
    r'<li>(?P<kilometers>.*)</li><li>(?P<motor>.*)</li><li>(?P<transmission>.*)</li>' #(1.) number of km, (2.) type of motor. (3.) type of transmission

)



def writing_data_json():
    cars = []
    count = 1
    for i in range(len(page_saving.brands)):
        for j in range(20):
            content = tools.file_content(f'captured_data/{page_saving.brands[i]}/{page_saving.brands[i]}_page_{j+1}.html')
            for match in re.finditer(pattern, content):
                count += 1
                cars.append(match.groupdict())
            tools.write_json(cars, f'car_files_json/{page_saving.brands[i]}.json') 
    print(count)
