import requests
from lxml import html
headers = {
    "accept" :  "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "accept-encoding" : "gzip, deflate, sdch, br",
    "accept-language" : "en-US,en;q=0.8,ms;q=0.6",
    "user-agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
}
url = "https://www.linkedin.com/in/shubhamshrivastav/"
r = requests.get(url, headers=headers)
print(r.content)
print(r.status_code)
root = html.fromstring(r.content)
print(root)