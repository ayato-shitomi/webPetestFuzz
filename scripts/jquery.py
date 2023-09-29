# 適当にやってみて Index of が入っていないことを確認する

import requests
import re
from . import utils

def main(arg):
	param = ["", "index.html", "index"]
	info = []
	for i in param:
		url = arg + "/" + i
		res = utils.send_request(url)
		if res.status_code == 200:
			line = res.text.split("\n")
			for j in line:
				if "jquery" in j:
					match = re.search(r'([^/]+)\.js', j)
					if match:
						version = match.group()
						utils.output("Found %s"%version,1)
					f = False
					for i in info:
						if i[0] == version:
							f = True
							break
					if f == False:
						info.append([version, url])

	return info
