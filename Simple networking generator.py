def restart():
	reset = input("\n" "Need another command? (Y/N): ").lower()		
	if reset == str("y"):
		if True:
			reset = main()
	elif reset == str("n"):
		reset = print("Good bye." "\n")
		quit()
	elif reset != str("y") or str("n"):
		if True:
			restart()

def main():
	userinput = input("Type 'help', or insert command: ").lower() 											

	def ospfprocess():
		try:
			process_variable = int(input("Insert an OSPF process number between 1 and 65535: "))
			ospf_area = int(input("Insert an ospf area between 0 and 4294967295: "))
			if process_variable >= 1 and process_variable <= 65535:
				if ospf_area >= 0 and ospf_area <= 4294967295:
					return str(process_variable), str(ospf_area)
		except (ValueError, TypeError, AttributeError):
			print("Invalid inputs, try again ")
			ospfprocess()

	if userinput == ("ospf"):	
		ospf_pro_and_area = ospfprocess()							
		ospf_net = input("Insert the ospf network: ")	
		ospf_mask = input("Insert the wildcard mask ")								
		ospf = ("\n" "enable" "\n" "configure terminal" "\n" "router ospf " + str(ospf_pro_and_area[0]) + "\n" "network " + ospf_net + " " + ospf_mask + " " + "area " + str(ospf_pro_and_area[1]))
		print(ospf)
		
	if userinput == ("rip"):
		ripnetwork = input("Insert ip subnet: ")
		ripver = input("RIP version 1 or 2? ")
		ripver = ("Version " + str(ripver))
		rip = ("\n" "enable" "\n" "configure terminal" "\n" "router rip " "\n" "network " + str(ripnetwork) + "\n" + str(ripver))
		print(rip)

	if userinput == ("stp"): 	
		stp = ("\n" "enable" "\n" "configure terminal" "\n" "spanning-tree mode rapid-pvst" "\n" "spanning tree vlan 1 root primary" "\n")
		print(stp)

	if userinput == ("ip"):	
		subnet = input("Insert your ip subnet: ")											
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
			print("\n" "ip address " + str(subnet) + " 255.255.255.0" "\n")

	def vlaninput():
		try:
			vlan_num = int(input("Insert a VLAN ID between 1-1005: "))
			if vlan_num >= 1 and vlan_num <= 1005:
				return str(vlan_num)
		except (ValueError, TypeError, AttributeError):
			print("Invalid inputs, try again ")
			vlaninput()

	if userinput == ("vlan"):	
			vlan_num = vlaninput()											
			vlan = ("\n" "enable" "\n" "configure terminal" "\n" "vlan " + str(vlan_num) + "\n" "interface */*" "\n" "switchport mode access" "\n" "switchport access vlan " + str(vlan_num))
			print(vlan)

	if userinput == ("password"): 
		pass_input = input("Insert your password: ")											
		secret_ask = input("Do you want a secret password? (Y/N): ").lower()
		if secret_ask == str("y"):
			secret_ask = input("Insert your secret password: ")								
			secret_enable = ("enable secret " + secret_ask + "\n")
		elif secret_ask == str("n"):
			secret_enable = ("")
		password = ("\n" "enable" "\n" "configure terminal" "\n" "enable password " + str(pass_input) + "\n" + str(secret_enable) + "service password-encryption")
		print(password)

	if userinput == ("cdp"): 
		cdp = input("Run or disable CDP? ").lower() 										
		if cdp == str("run"):
			cdp = ("cdp run" "\n" "Note: CDP is enabled by default")
		elif cdp == str("disable"):
			cdp = ("no cdp run")
		print("\n" "enable" "\n" "configure terminal" "\n" + cdp)

	if userinput == ("port security"):	
		port_sec_max = input("Max number of mac addresses allowed: ") 						
		port_sec_maxmac = ("switchport port-security maximum " + str(port_sec_max))
		port_sec_opt = input("Mac or Sticky? ").lower()										
		if port_sec_opt == ("mac"):
			port_sec_mac_ask = input("Insert mac address: ") 								
			port_sec_mac = ("switchport port-security mac-address " + port_sec_mac_ask)
		elif port_sec_opt == ("sticky"): 														
			port_sec_mac = ("switchport port-security mac-address sticky ")
		port_security = ("\n" "enable" "\n" "configure terminal" "\n" "interface */*" "\n" "switchport mode access" "\n" "switchport port-security " "\n" + port_sec_maxmac + "\n" + str(port_sec_mac))
		print(port_security)

	if userinput == ("speed"):	
		speed = ("\n" "enable" "\n" "configure terminal" "\n" "interface */*" "\n" "speed 100" "\n")
		print(speed)

	if userinput == ("duplex"):	
		duplexask = input("Full or half")
		duplex = ("\n" "enable" "\n" "configure terminal" "\n" "interface */*" "duplex " + str(duplexask) + "\n")
		print(duplex)

	if userinput == ("portfast"):
		portfast = ("enable" "\n" "configure terminal" "\n" "spanning-tree portfast default ")
		print(portfast)

	if userinput == ("help"):		
		helptext = ("\n" "The commands include: ospf, ip, stp, vlans, password, port security, cdp, rip, speed, duplex, portfast " "\n")
		print(helptext)
		main()

	if userinput != list[str("ospf"), str("ip"), str("stp"), str("vlan"), str("passwords"), str("port security"), str("cdp"), str("rip"), str("speed"), str("duplex"), str("portfast"), int()]:
		if True:
			restart()
	
	restart()	

main()
