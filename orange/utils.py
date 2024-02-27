from time import sleep
import requests as req
from bs4 import BeautifulSoup
from getpass import getpass
from sys import stdout
from os import path
import re
session = req.Session()
session.headers.update({
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0'
	})

# Check or/and save IP at ip-modem.config
def input_modem_ip():
	IP = "192.168.0.1"
	user_input = input('Modem ip (default : 192.168.0.1 > ')

	if len(re.findall('(?:(?:\d|[01]?\d\d|2[0-4]\d|25[0-5])\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d|\d)(?:\/\d{1,2})?', user_input)) != 0:
		IP = user_input
	return IP

def check_ip_save():
	if path.exists('ip-modem.config'):
		return open('ip-modem.config', 'r+').read()
	else:
		return input_modem_ip()

def save_valide_ip(IP):
	if not path.exists('ip-modem.config'):
		with open('ip-modem.config', 'w+') as file:
			file.write(IP)

def setup():
	global IP
	IP = check_ip_save()
	if ("Cable network" in req.get(f"http://{IP}", timeout=3).text):
		save_valide_ip(IP)
		return True
	else:
		print("Default or input IP is not working")
		return False
			
def clear():
	stdout.write("\033[H\033[J")

def get_pub_ip():
	return BeautifulSoup(req.get(f"http://{IP}/overview.asp")
	.text, "html.parser").find("span", attrs={"class": "severFontSize fontStyle01"}).get_text()

def restart_local():
	session.post(f"http://{IP}/goform/OrgNetworkRestart", data={"AskRgRestart": 1})
	sleep(8)
	print(
		"New public ip adress : "
		+ get_pub_ip()
	)

def restart_modem():
	session.post(f"http://{IP}/goform/OrgRestart", data={"AskRgRestart": 1})
	clear()
	print("the modem will restart...")
	exit()

def stats_resolver(login):
	return [
		str(i).split(">")[1].split("<")[0]
		for i in BeautifulSoup(login.text, "html.parser").find_all(
			"span", {"class": "severFontSize fontStyle01"}
		)
	]

