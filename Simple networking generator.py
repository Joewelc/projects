def restart():
	reset = input("\n" "Need another command? (Y/N): ").lower()		
	if reset == str("y"):
		if True:
			reset = main()
	elif reset == str("n"):
		reset = print("Good bye.")
		quit()
	elif reset != str("y") or str("n"):
		if True:
			restart()

def main():
	userinput = input("Type 'help', or insert command: ").lower() 											

	def ospfprocess():
		try:
			process_variable = int(input("Insert an OSPF process number between 1 and 65535: "))
			if process_variable >= 1 and process_variable <= 65535:
				return str(int(process_variable))
		except ValueError:
			print("Please use a number between 1 and 65535")
			ospfprocess()

	if userinput == ("ospf"):	
		if userinput == ("ospf"):	
			ospfval = ospfprocess()						
			ospf_area_ask = input("Insert ospf area: ")		
			ospf_net = input("Insert the ospf network: ")	
			ospf_mask = input("Insert the wildcard mask ")								
			ospf_area = ("area " + ospf_area_ask)
			ospf = ("\n" "Enable" "\n" "configure terminal" "\n" "router ospf " + str(ospfval) + "\n" "network " +ospf_net + " " + ospf_mask + " " +  ospf_area)
			print(ospf)
		
	if userinput == ("rip"): 	
		rip = ("\n" "Enable" "\n" "configure terminal" "\n" "router rip " "\n" "network *IP subnet and mask* " "\n" "version 2" "\n")
		print(rip)

	if userinput == ("stp"): 	
		stp = ("\n" "Enable" "\n" "configure terminal" "\n" "spanning-tree mode rapid-pvst" "\n" "spanning tree vlan 1 root primary" "\n")
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

	if userinput == ("vlan"):	
		vlan_num = input("Insert a Vlan number: ")											
		vlan = ("Enable" "\n" "configure terminal" "\n" "vlan " + vlan_num + "\n" "interface */*" "\n" "switchport mode access" "\n" "switchport access vlan " + vlan_num)
		print(vlan)

	if userinput == ("password"): 
		pass_input = input("Insert your password: ")											
		secret_ask = input("Do you want a secret password? (Y/N): ").lower()
		if secret_ask == str("y"):
			secret_ask = input("Insert your secret password: ")								
			secret_enable = ("enable secret " + secret_ask + "\n")
		elif secret_ask == str("n"):
			secret_enable = ("")
		password = ("Enable" "\n" "configure terminal" "\n" "enable password " + str(pass_input) + "\n" + str(secret_enable) + "service password-encryption")
		print(password)

	if userinput == ("cdp"): 
		cdp = input("Run or disable CDP? ").lower() 										
		if cdp == str("run"):
			cdp = ("cdp run" "\n" "Note: CDP is enabled by default")
		elif cdp == str("disable"):
			cdp = ("no cdp run")
		print("Enable" "\n" "configure terminal" "\n" + cdp)

	if userinput == ("port security"):	
		port_sec_max = input("Max number of mac addresses allowed: ") 						
		port_sec_maxmac = ("switchport port-security maximum " + str(port_sec_max))
		port_sec_opt = input("Mac or Sticky? ").lower()										
		if port_sec_opt == ("mac"):
			port_sec_mac_ask = input("Insert mac address: ") 								
			port_sec_mac = ("switchport port-security mac-address " + port_sec_mac_ask)
		elif port_sec_opt == ("sticky"): 														
			port_sec_mac = ("switchport port-security mac-address sticky ")
		port_security = ("Enable" "\n" "configure terminal" "\n" "interface */*" "\n" "switchport mode access" "\n" "switchport port-security " "\n" + port_sec_maxmac + "\n" + str(port_sec_mac))
		print(port_security)

	if userinput == ("speed"):	
		speed = ("\n" "Enable" "\n" "configure terminal" "\n" "interface */*" "\n" "speed 100" "\n")
		print(speed)

	if userinput == ("duplex"):	
		duplex = ("\n" "Enable" "\n" "configure terminal" "\n" "interface */*" "duplex full" "\n")
		print(duplex)

	if userinput == ("portfast"):
		portfast = ("Enable" "\n" "configure terminal" "\n" "spanning-tree portfast default ")
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
