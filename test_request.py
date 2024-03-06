import requests

url = 'https://www.w3schools.com/python/demopage.php'
myobj = {'text': 'Hello! I am Wei Soon.'}

x = requests.post(url, json = myobj)

print(x.text)