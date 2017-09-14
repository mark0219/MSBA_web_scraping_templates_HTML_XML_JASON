
import requests
from lxml import objectify

parameter = 'tavg'
state_id = 44
division_id = 0
month = 8
num_periods = 6
year = '2016'

base_link = 'https://www.ncdc.noaa.gov/temp-and-precip/climatological-rankings/download.xml?'
add_on_link = 'parameter=%s&state=%s&div=%s&month=%s&periods[]=%s&year=%s'
insert_variables = (parameter, state_id, division_id, month, num_periods, year)
add_on_link = add_on_link % insert_variables
link_request = base_link + add_on_link

response = requests.get(link_request).content
root = objectify.fromstring(response)

my_wm_username = 'czhang11'

print my_wm_username
print 'Value: ', root["data"]["value"]
print 'Twentieth Century Mean: ', root["data"]["twentiethCenturyMean"]
print 'Low Rank: ', root["data"]["lowRank"]
print 'High Rank: ', root["data"]["highRank"]