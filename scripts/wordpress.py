# 見るべきは /wp-content/uploads/ のディレクトリリスティング
# adminコンソールへのアクセス

import requests
from . import utils

param = [
	"admin",
	"wp-admin",
	"wp-admin/",
	"wp-admin/admin.php",
	"login",
]

def chk_wordpress(url):
	res = utils.send_request(url)
	if res.status_code == 200:
		if "wordpress" in res.text.lower():
			return True
	return False

def main(arg):
	urls = []
	# wordpressが存在するかチェック
	if chk_wordpress(arg) == False:
		return urls
	# wp-content/uploads/ のディレクトリリスティング
	res = utils.send_request(arg + "/wp-content/uploads/")
	if res.status_code == 200:
		if "index of" in res.text.lower():
			urls.append(["Wordpress Directory listing", arg + "/wp-content/uploads/"])
		if "listing" in res.text.lower():
			urls.append(["Wordpress Directory listing", arg + "/wp-content/uploads/"])
	# adminコンソールへのログインぺージ
	for i in param:
		url = arg + "/" + i
		res = utils.send_request(url)
		if res.status_code == 200:
			urls.append(["Wordpress Login page",url])
	return urls
