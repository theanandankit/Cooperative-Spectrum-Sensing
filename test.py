import requests
import time

# URL = "http://localhost:5000/mine_block"
# headers = {'Content-Type': 'application/json', 'Accept' : 'application/json'}
# data = [
#     {
#         'value' : 60
#     }
# ]

# start = int(time.time()*1000)
# r = requests.post(url = URL, json = data, headers = headers)
# finish = int(time.time()*1000)

# print(finish - start)
# print(r.text)

G_url = "http://localhost:5000/mine_block"

start = int(time.time()*100000)
headers = {'Content-Type': 'application/json', 'Accept' : 'application/json'}

r = requests.get(url = G_url)
finish = int(time.time()*100000)

print(finish - start)
