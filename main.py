import os
from scripts import utils
from scripts import robots
from scripts import readme
from scripts import dir_listing
from scripts import git
from scripts import jquery
from scripts import wordpress
from scripts import server

try:
	arg = os.sys.argv[1]
except:
	utils.output("No argument given", 2)
	utils.output("Usage: python main.py <Target URL>", 2)
	exit()

def run(arg):
	credential = []

	# 疎通チェック
	print()
	utils.output("Running basic check", 0)
	try:
		res = utils.send_request(arg)
	except:
		utils.output("Basic check failed", 2)
		exit()
	
	# 利用するモジュール一覧
	modules = [robots, readme, dir_listing, git, jquery, wordpress, server]

	for module in modules:
		print()
		module_name = str(module.__name__).replace("scripts.", "")
		utils.output("Running %s check"%(module_name), 0)
		try:
			credential.extend(module.main(arg))
		except:
			utils.output("%s check"%(module_name), 2)
		
	return credential

if __name__ == '__main__':
	utils.welcome()
	utils.output("Starting...", 0)
	if (arg.startswith("http://") or arg.startswith("https://")) == False:
		utils.output("Target URL must start with http:// or https://", 2)
		exit()
	elif arg.endswith("/"):
		arg = arg[:-1]
	utils.output("Target is: %s/"%arg, 0)
	result = run(arg)

	print()
	if len(result) == 0:
		utils.output("RESULT:", 2)
		print("\n\t- No results -")
		exit()
	utils.output("RESULT:\n", 1)
	for i in result:
		if isinstance(i, list):
			print("\t👉\033[32m", i[0], "\033[0mwas found on", i[1])
		else:
			print("\t", i)

