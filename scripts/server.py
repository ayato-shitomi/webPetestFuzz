import requests
from . import utils


def main(arg):
	urls = []
	res = utils.send_request(arg)
	req_header = res.headers.get("Server")
	if req_header != None:
		urls.append(["Server version", "response header: " + req_header])
		return urls
	return urls
