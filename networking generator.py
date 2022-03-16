userinput = input("I can help with Cisco commands, type 'help', or insert command: ").lower() # Command input
err = ("NULL") 	
																		#The default error message
if userinput == ("ospf"):
	ospfval = input("Insert an OSPF process number ")									# OSPF process input
	ospf_area_ask = input("Insert ospf area ")											# OSPF area input
	ospf_area = ("area " + ospf_area_ask)
	ospf = ("Enable" "\n" "configure terminal" "\n" "router ospf " + ospfval + "\n" "network *IP subnet and wildcard mask* " + ospf_area)
	print(ospf)

if userinput == ("rip"):
	rip = ("Enable" "\n" "configure terminal" "\n" "router rip " "\n" "network *IP subnet and mask* " "\n" "version 2")
	print(rip)

if userinput == ("stp"):
	stp = ("Enable" "\n" "configure terminal" "\n" "spanning-tree mode rapid-pvst" "\n" "spanning tree vlan 1 root primary")
	print(stp)

if userinput == ("ip"):
	subnet = input("Insert your ip subnet ")											# Ip input
	submask = input("What is the subnet mask? 0, 128, 64, 32, 16, etc ")				# Subnet input
	if int(submask) == (128):
		print("ip address " + str(subnet) + " 255.255.255.128")
	elif int(submask) == (64):
		print("ip address " + str(subnet) + " 255.255.255.192")
	elif int(submask) == (32):
		print("ip address " + str(subnet) + " 255.255.255.224")
	elif int(submask) == (16):
		print("ip address " + str(subnet) + " 255.255.255.240")
	elif int(submask) == (8):
		print("ip address " + str(subnet) + " 255.255.255.248")
	elif int(submask) == (4):
		print("ip address " + str(subnet) + " 255.255.255.252")
	elif int(submask) == (2):
		print("ip address " + str(subnet) + " 255.255.255.254")
	elif int(submask) == (0):
		print("ip address " + str(subnet) + " 255.255.255.0")

if userinput == ("vlan"):
	vlan_num = input("Insert a Vlan number ")											# Vlans input
	vlan = ("Enable" "\n" "configure terminal" "\n" "vlan " + vlan_num + "\n" "interface */*" "\n" "switchport mode access" "\n" "switchport access vlan " + vlan_num)
	print(vlan)

if userinput == ("password"):
	pass_input = input("Insert your password ")											# Password input
	secret_ask = input("Do you want a secret password? Y/N ").lower()
	if secret_ask == str("y"):
		secret_ask = input("Insert your secret password ")								# Secret pass input
		secret_enable = ("enable secret " + secret_ask + "\n")
	if secret_ask == str("n"):
		secret_enable = ("")
	password = ("Enable" "\n" "configure terminal" "\n" "enable password " + str(pass_input) + "\n" + str(secret_enable) + "service password-encryption")
	print(password)

if userinput == ("cdp"):
	cdp = input("Run or disable CDP? ").lower() 										# CDP run or disable
	if cdp == str("run"):
		cdp = ("cdp run" "\n" "Note: CDP is enabled by default")
	if cdp == str("disable"):
		cdp = ("no cdp run")
	print("Enable" "\n" "configure terminal" "\n" + cdp)

if userinput == ("port security"):
	port_sec_max = input("Max number of mac addresses allowed: ") 						# Max macs
	port_sec_maxmac = ("switchport port-security maximum " + str(port_sec_max))
	port_sec_opt = input("Mac or Sticky? ").lower()										# Mac sticky question
	if port_sec_opt == ("mac"):
		port_sec_mac_ask = input("Insert mac address: ") 								# Mac address
		port_sec_mac = ("switchport port-security mac-address " + port_sec_mac_ask)
	if port_sec_opt == ("sticky"): 														# Sticky mac address
		port_sec_mac = ("switchport port-security mac-address sticky ")
	port_security = ("Enable" "\n" "configure terminal" "\n" "interface */*" "\n" "switchport mode access" "\n" "switchport port-security " "\n" + port_sec_maxmac + "\n" + str(port_sec_mac))
	print(port_security) 

if userinput == ("speed"):
	speed = ("Enable" "\n" "configure terminal" "\n" "interface */*" "speed 100")
	print(speed)

if userinput == ("duplex"):
	duplex = ("Enable" "\n" "configure terminal" "\n" "interface */*" "\n" "duplex full")
	print(duplex)

if userinput == ("help"):	#Shows current available commands
	help = ("The commands include: ospf, ip, stp, vlans, passwords, port security, cdp, rip, speed ")
	print(help)

def main():		#Main loop starts
	userinput = input("I can help with Cisco commands, type 'help', or insert command: ").lower() 
	err = ("NULL") 																			

	if userinput == ("ospf"):
		ospfval = input("Insert an OSPF process number ")									
		ospf_area_ask = input("Insert ospf area ")											
		ospf_area = ("area " + ospf_area_ask)
		ospf = ("Enable" "\n" "configure terminal" "\n" "router ospf " + ospfval + "\n" "network *IP subnet and wildcard mask* " + ospf_area)
		print(ospf)
		
	if userinput == ("rip"):
		rip = ("Enable" "\n" "configure terminal" "\n" "router rip " "\n" "network *IP subnet and mask* " "\n" "version 2")
		print(rip)

	if userinput == ("stp"):
		stp = ("Enable" "\n" "configure terminal" "\n" "spanning-tree mode rapid-pvst" "\n" "spanning tree vlan 1 root primary")
		print(stp)

	if userinput == ("ip"):
		subnet = input("Insert your ip subnet ")											
		submask = input("What is the subnet mask? 128, 64, 32, 16, etc ")					
		if int(submask) == (128):
			print("ip address " + str(subnet) + " 255.255.255.128")
		elif int(submask) == (64):
			print("ip address " + str(subnet) + " 255.255.255.192")
		elif int(submask) == (32):
			print("ip address " + str(subnet) + " 255.255.255.224")
		elif int(submask) == (16):
			print("ip address " + str(subnet) + " 255.255.255.240")
		elif int(submask) == (8):
			print("ip address " + str(subnet) + " 255.255.255.248")
		elif int(submask) == (4):
			print("ip address " + str(subnet) + " 255.255.255.252")
		elif int(submask) == (2):
			print("ip address " + str(subnet) + " 255.255.255.254")
		elif int(submask) == (0):
			print("ip address " + str(subnet) + " 255.255.255.0")

	if userinput == ("vlan"):
		vlan_num = input("Insert a Vlan number ")											
		vlan = ("Enable" "\n" "configure terminal" "\n" "vlan " + vlan_num + "\n" "interface */*" "\n" "switchport mode access" "\n" "switchport access vlan " + vlan_num)
		print(vlan)

	if userinput == ("password"):
		pass_input = input("Insert your password ")											
		secret_ask = input("Do you want a secret password? Y/N ").lower()
		if secret_ask == str("y"):
			secret_ask = input("Insert your secret password ")								
			secret_enable = ("enable secret " + secret_ask + "\n")
		if secret_ask == str("n"):
			secret_enable = ("")
		password = ("Enable" "\n" "configure terminal" "\n" "enable password " + str(pass_input) + "\n" + str(secret_enable) + "service password-encryption")
		print(password)

	if userinput == ("cdp"):
		cdp = input("Run or disable CDP? ").lower() 										
		if cdp == str("run"):
			cdp = ("cdp run" "\n" "Note: CDP is enabled by default")
		if cdp == str("disable"):
			cdp = ("no cdp run")
		print("Enable" "\n" "configure terminal" "\n" + cdp)

	if userinput == ("port security"):
		port_sec_max = input("Max number of mac addresses allowed: ") 						
		port_sec_maxmac = ("switchport port-security maximum " + str(port_sec_max))
		port_sec_opt = input("Mac or Sticky? ").lower()										
		if port_sec_opt == ("mac"):
			port_sec_mac_ask = input("Insert mac address: ") 								
			port_sec_mac = ("switchport port-security mac-address " + port_sec_mac_ask)
		if port_sec_opt == ("sticky"): 														
			port_sec_mac = ("switchport port-security mac-address sticky ")
		port_security = ("Enable" "\n" "configure terminal" "\n" "interface */*" "\n" "switchport mode access" "\n" "switchport port-security " "\n" + port_sec_maxmac + "\n" + str(port_sec_mac))
		print(port_security)

	if userinput == ("speed"):
		speed = ("Enable" "\n" "configure terminal" "\n" "interface */*" "\n" "speed 100")
		print(speed)

	if userinput == ("duplex"):
		duplex = ("Enable" "\n" "configure terminal" "\n" "interface */*" "duplex full")
		print(duplex)

	if userinput == ("help"):						#Shows current available commands
		help = ("The commands include: ospf, ip, stp, vlans, passwords, port security, cdp, rip ")
		print(help)

	reset = input("Need another command? (Y/N) ").lower()			#reset command after loop			
	if reset == str("y"):
		if True:
			reset = main()
		if False:
			reset = quit()

# Main loop end

reset = input("Need another command? (Y/N) ").lower()	#restarts or quits script after 1st command input		
if reset == str("y"):
	if True:
		reset = main()
	if False:
		reset = quit()
