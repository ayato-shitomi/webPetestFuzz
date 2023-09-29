
import requests
from . import utils

param = [
	"readme.md",
	"README.md",
	"readme.html",
	"readme.txt",
	"README.txt",
	"readme",
	"README",
	"readme.php"
]

def main(arg):
	urls = []
	for i in param:
		url = arg + "/" + i
		res = utils.send_request(url)
		if res.status_code == 200:
			urls.append(["Readme file",url])
	return urls
