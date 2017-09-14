import requests
from bs4 import BeautifulSoup as bsoup

search_url = 'http://publicinterestlegal.org/county-list/'
response = requests.get(search_url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}).content
            
parsed_html = bsoup(response, 'lxml')
target_rows = parsed_html.find_all('tr')

total_table =[]
for row in target_rows:
    new_row = []
    for x in row.find_all('td'):
        new_row.append(x.text.encode("ascii",'ignore'))
    total_table.append(new_row)

print 'W&M User Name: ', 'czhang11'
print 'Number of Rows: ', len(total_table)

#print total_table
print total_table