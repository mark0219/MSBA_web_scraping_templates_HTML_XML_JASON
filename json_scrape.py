import requests

my_wm_username = 'czhang11'
search_url = 'http://buckets.peterbeshai.com/api/?player=201939&season=2015'
response = requests.get(search_url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}).content
 
numJumpShotsAttempt = 0
numJumpShotsMade = 0
percJumpShotMade = 0.0

for shot in response.json():
    if shot['ACTION_TYPE'] == 'Jump Shot':
        numJumpShotsAttempt += 1
    if (shot['ACTION_TYPE'] == 'Jump Shot') & (shot['EVENT_TYPE'] == 'Made Shot'):
        numJumpShotsMade += 1
        
percJumpShotMade = float(numJumpShotsMade) / numJumpShotsAttempt

print 'W&M ID: ', my_wm_username
print 'Jump Shots Attempted: ', numJumpShotsAttempt
print 'Jump Shots Made: ', numJumpShotsMade
print 'Percentage of Jump Shots Made: ', percJumpShotMade