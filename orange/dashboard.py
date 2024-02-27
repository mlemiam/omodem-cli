from requests import post, get
from orange.utils import getpass, get_pub_ip, restart_local, restart_modem, stats_resolver, check_ip_save, clear
IP = check_ip_save()

def dash():
	net_stats = [
		"🌐 Wifi",
		"🌍 Network access",
		"🔌 Wired network"
	]

	status = stats_resolver(get(f"http://{IP}", timeout=3))

	net_stats_index = 0
	for stats in net_stats:
		print(
				stats, f": {status[net_stats_index]}",
				end=None
			)
		net_stats_index += 1

	if (
		"Incorrect password !"
		in post(
			f"http://{IP}/goform/OrgLogin",
			data={"OrgPassword": getpass("Pass > ")},
		).text
	):
		print("❌ Incorrect password")
	else:
		print(
			"Public ip adress : "
			+ get_pub_ip()
		)

		choice = input(
	"""Choose an option :
		1 - Change ip adress (restart local network)
		2 - Restart modem
		x - exit
	> """
			)	
		match choice:
			case "1":
				restart_local()
			case "2":
				restart_modem()
			case "x":
				clear()
				exit()
			case _:
				print("❌ Invalid option")
