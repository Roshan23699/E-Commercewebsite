print("enter the website u want to block")
a = input()
ip = "127.0.0.1"
host = "/etc/hosts"
file1 = open(host, "r+")
file1.truncate()
website_list = file1.read()
if a in website_list:
	pass
else:
	file1.write(ip+" "+ a)
	print("website blocked successfully")
