import requests
from . import utils

def main(arg):
	url = arg + "/robots.txt"
	res = utils.send_request(url)
	if res.status_code == 200:
		return [["robots.txt",url]]
	return False

