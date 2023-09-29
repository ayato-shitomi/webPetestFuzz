# 適当にやってみて Index of が入っていないことを確認する

import requests
from . import utils

def main(arg):
	param = ["js", "css", "src", "srcs"]
	urls = []
	for i in param:
		url = arg + "/" + i
		res = utils.send_request(url)
		if res.status_code == 200:
			if "Index of" in res.text:
				urls.append(["Directory listing", url])
			if "listing" in res.text:
				urls.append(["Directory listing", url])
	return urls
