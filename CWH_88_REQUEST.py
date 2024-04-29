import requests

url = "https://www.freshmenu.com/"

r = requests.get(url)
print(r.text)