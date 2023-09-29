import requests
from . import utils

def main(arg):
	url = arg + "/.git/HEAD"
	res = utils.send_request(url)
	if res.status_code == 200:
		return [["Git file",url]]
	return False

