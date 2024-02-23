from bs4 import BeautifulSoup
import requests

end = False

def print_url(url):
	global end
	if url == None:
		return
	file = requests.get(url)
	content = file.content.decode('utf-8')
	if 'flag' in content:
		print(url + '->' + content)
		end = True


def parse(url):
	global end
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	a = soup.find_all('a')
	if len(a) == 0:
		return None
	a.pop(0)
	if len(a) == 1:
		print_url(url + a[0].get('href'))
	else:
		for i in range(len(a)-1, 0, -1):
			if end == True:
				break
			parse(url+a[i].get('href')+"/")
	return a

data = parse('http://192.168.56.110/.hidden/')
