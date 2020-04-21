import json
import requests
import re
import tools
import page_saving

pattern_data = (
    
    r'<!--------------------- DESCRIPTION  ------------------->'
    r'\s+<a class=".*" href=".*">\s+'
    r'<span>(?P<brand>.*?)\s(?P<model>.*)\.*</span>' #exctrating car brand and model
    r'\s+</a>\s+'
    r'<!--------------------- DATA  ------------------->'
    r'\s+<ul>\s+'
    r'<li>\w*\s[1]\.\w*\W(?P<first_registration>.*)</li>' #data of first registration
    r'\s+'
    r'<*l*i*>*(?P<kilometers>\d*?)\s\w*<*/*l*i*>*<*l*i*>*(?P<engine>\w*).*<*/*l*i*>*<li>(?P<transmission>\w*).*</li>' #(1.) number of km, (2.) type of motor. (3.) type of transmission

)

pattern_price = (
    r'<!------------ REDNA OBJAVA CENE ------------>'
    r'\s+<div class="ResultsAdPriceTXTMiddle">\s+'
    r'\s+<div class=".*">(?P<price>.*)\W</div>\s+'

)


def writing_data_and_price_json_csv():
    cars_data = []
    cars_price = []
    # count = 0
    # count1 = 0
    for i in range(len(page_saving.brands)):
        for j in range(20):
            content = tools.file_content(f'captured_data/{page_saving.brands[i]}/{page_saving.brands[i]}_page_{j+1}.html')
            for match_data in re.finditer(pattern_data, content): # for loop for appending car data
                # count += 1
                # print(match_data.groupdict())
                cars_data.append(match_data.groupdict())
            for match_price in re.finditer(pattern_price, content): # for loop for appending car prices
                # count1 += 1
                cars_price.append(match_price.groupdict())
    # print(count, count1)
    tools.write_csv(cars_price, ['price'], 'cars_price.csv')
    tools.write_json(cars_price, 'cars_price.json')
    tools.write_json(cars_data, 'cars_data.json') 
    tools.write_csv(cars_data, ['brand', 'model', 'first_registration', 'kilometers', 'engine', 'transmission'], 'cars_data.csv')
    
def fix_price(filename):
    # "C:/Users/User/Documents/GitHub/Projektna-naloga-prog.1/cars_price.csv"
    content = tools.file_content(filename)
    cars_price = content.replace('.','')
    with open('cars_price.csv', 'w') as fl:
        fl.truncate()
        fl.write(cars_price)
