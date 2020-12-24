import pandas as pd
from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.datawaveservices.in/dws/work/UpdateForm/1160542/181')
soup = BeautifulSoup(page.content, 'html.parser')

# print(soup)
# print(soup.find_all('a')) # only print a tag

week = soup.find(id='tlClogo')
print(week) # print the whole html code inside id seven-day-forecast-body

items = week.find_all(class_='tombstone-container')
# print(item[0])

# print(items[0].find(class_='period-name').get_text())
# print(items[0].find(class_='short-desc').get_text())
# print(items[0].find(class_='temp').get_text())

print()
period_name = [item.find(class_='period-name').get_text() for item in items]
# print(period_name)

short_desc = [item.find(class_='short-desc').get_text() for item in items]
# print(short_desc)

temperatures = [item.find(class_='temp').get_text() for item in items]
# print(temperatures)

weather_stuff = pd.DataFrame(
                {
                    'Period': period_name,
                    'short-desc': short_desc,
                    'temperatures': temperatures
                })
print(weather_stuff)

weather_stuff.to_csv('result.csv')
