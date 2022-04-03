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
			vlan_int = input("Insert the interface type (serial, gig, fa, eth, etc): ").lower()
			vlan_int = "interface " + str(vlan_int)
			vlan_int_num = input("Insert the interface number (*/*): ").lower()
			if vlan_num >= 1 and vlan_num <= 1005:
				return str(vlan_num), str(vlan_int), str(vlan_int_num)
		except (ValueError, TypeError, AttributeError):
			print("Invalid inputs, try again ")
			vlaninput()

	if userinput == ("vlan"):	
			vlan_ret = vlaninput()											
			vlan = ("\n" "enable" "\n" "configure terminal" "\n" "vlan " + str(vlan_ret[0]) + "\n" + str(vlan_ret[1]) + " " + str(vlan_ret[2]) + "\n" "switchport mode access" "\n" "switchport access vlan " + str(vlan_ret[0]))
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
		port_sec_int = input("Insert the interface type (serial, gig, fa, eth, etc): ").lower()	
		port_sec_int = "interface " + str(port_sec_int)
		port_sec_int_num = input("Insert the interface number (*/*): ").lower()							
		if port_sec_opt == ("mac"):
			port_sec_mac_ask = input("Insert mac address: ") 								
			port_sec_mac = ("switchport port-security mac-address " + port_sec_mac_ask)
		elif port_sec_opt == ("sticky"): 														
			port_sec_mac = ("switchport port-security mac-address sticky ")
		port_security = ("\n" "enable" "\n" "configure terminal" "\n" + str(port_sec_int) + str(port_sec_int_num) + "\n" "switchport mode access" "\n" "switchport port-security " "\n" + port_sec_maxmac + "\n" + str(port_sec_mac))
		print(port_security)

	if userinput == ("speed"):	
		speed_int = input("Insert the interface type (serial, gig, fa, eth, etc): ").lower()
		speed_int = "interface " + str(speed_int)
		speed_int_num = input("Insert the interface number (*/*): ").lower()
		speed = ("\n" "enable" "\n" "configure terminal" "\n" + str(speed_int) + " " + str(speed_int_num) + "\n" "speed 100")
		print(speed)

	if userinput == ("duplex"):	
		duplexask = input("Full or half: ").lower()
		duplex_int = input("Insert the interface type (serial, gig, fa, eth, etc): ").lower()
		duplex_int = "interface " + str(duplex_int)
		duplex_int_num = input("Insert the interface number (*/*): ").lower()
		duplex = ("\n" "enable" "\n" "configure terminal" "\n" + str(duplex_int) + " " + str(duplex_int_num) + "\n" "duplex " + str(duplexask) + "\n")
		print(duplex)

	if userinput == ("portfast"):
		portfast = ("enable" "\n" "configure terminal" "\n" "spanning-tree portfast default ")
		print(portfast)

	def aclcreator():
		try:
			acl_number = int(input("Input an access list number (1-99) or (100-199): "))
			acl_arguement = input("Permit or Deny?: ")
			if acl_number <= 99:
				acl_address = input("Input the ip address of network: ")
				acl_wild = input("Input the wildcard mask: ")
				return int(acl_number), str(acl_arguement), str(acl_address), str(acl_wild)
			elif acl_number <= 199:
				acl_type = input("Which protocol? (ip, tcp): ").lower()
				if acl_type == str("ip"):
					acl_source = input("Input a host source address: ")
					acl_dest = input("Input a destination address: ")
					acl_dest_wild = input("Input the destination wildcard: ")
					return int(acl_number), str(acl_arguement), str(acl_type), str(acl_source), str(acl_dest), str(acl_dest_wild)
				if acl_type == str("tcp"):
					acl_source = input("Input a host source address: ")
					acl_source_wild = input("Input the source wildcard ")
					acl_dest = input("Input a destination address: ")
					acl_dest_wild = input("Input the destination wildcard: ")
					acl_tcp_port = input("Which port? (ftp, pop3, smtp, telnet, www): ")
					acl_tcp_port = ("eq " + acl_tcp_port)
					return int(acl_number), str(acl_arguement), str(acl_type), str(acl_source), str(acl_source_wild), str(acl_dest), str(acl_dest_wild), str(acl_tcp_port), 
		except (ValueError, TypeError, AttributeError):
			print("Invalid inputs, try again ")
			aclcreator()

	if userinput == ("acl"):	
			acl_list = aclcreator()
			if acl_list[0] <= 99:
				acl = ("\n" "enable" "\n" "configure terminal" "\n" "access-list " + str(int(acl_list[0])) + " " + str(acl_list[1]) + " " + str(acl_list[2]) + " " + str(acl_list[3]))
				print(acl)
			elif acl_list[0] <= 199:
				if acl_list[2] == str("tcp"):
					acl = ("\n" "enable" "\n" "configure terminal" "\n" "access-list " + str(int(acl_list[0])) + " " + str(acl_list[1]) + " " + str(acl_list[2]) + " " + str(acl_list[3]) + " " + str(acl_list[4]) + " " + str(acl_list[5]) + " " + str(acl_list[6]) + " " + str(acl_list[7]))
					print(acl)
				elif acl_list[2] == str("ip"):
					acl = ("\n" "enable" "\n" "configure terminal" "\n" "access-list " + str(int(acl_list[0])) + " " + str(acl_list[1]) + " " + str(acl_list[2]) + " " + str(acl_list[3]) + " " + str(acl_list[4]) + " " + str(acl_list[5]))
					print(acl)	

	def natcreator():
			try:
				nat_ask = input("Create pool, or Translation?: ").lower()
				if nat_ask == str("pool"):
					nat_pool = input("Input the name of the pool: ").lower()
					nat_pool_start = input("Starting address: ")
					nat_pool_end = input("Ending address: ")
					nat_netmask = input("Insert the mask: ")
					pool_total = ("enable" "\n" "configure terminal" "\n" "ip nat " + str(nat_pool) + " " + str(nat_pool_start) + " " + str(nat_pool_end) + " " + str(nat_netmask))
					return  str(nat_ask), str(pool_total)
				elif nat_ask == str("translation"):
					nat_trans_ask = input("Input the source (list or static): ").lower()
					if nat_trans_ask == str("list"):
						nat_list = input("Input the ACL number: ")
						nat_trans_ask = input("Interface or pool?: ").lower()
						if nat_trans_ask == str("interface"): 
							nat_overload = input("Do you want to enable PAT? (Y/N): ").lower()
							if nat_overload == str("y"):
								nat_overload = str("overload")
								nat_list_translation = ("enable" "\n" "configure terminal" "\n" "ip nat inside source list " + str(nat_list) + "interface <TYPE */*> " + str(nat_overload))
								return str(nat_ask), str(nat_list_translation)
							elif nat_overload == str("n"):
								nat_overload = str(" ")
								nat_list_translation = ("enable" "\n" "configure terminal" "\n" "ip nat inside source list " + str(nat_list) + "interface <TYPE */*> " + str(nat_overload))
								return str(nat_ask), str(nat_list_translation)
						elif nat_trans_ask == str("pool"):
							nat_pool_name = input("Insert pool name: ")
							nat_pool = str(nat_pool_name)
							nat_overload = input("Do you want to enable PAT? (Y/N): ").lower()
							if nat_overload == str("y"):
								nat_overload = str("overload")
								nat_list_translation = ("enable" "\n" "configure terminal" "\n" "ip nat inside source list " + str(nat_list) + "pool " + str(nat_pool) + " " + str(nat_overload))
								return str(nat_ask), str(nat_list_translation)
							elif nat_overload == str("n"):
								nat_overload = str(" ")
								nat_list_translation = ("enable" "\n" "configure terminal" "\n" "ip nat inside source list " + str(nat_list) + "pool " + str(nat_pool) + " " + str(nat_overload))
								return str(nat_ask), str(nat_list_translation)
					elif nat_trans_ask == str("static"):
						nat_list_inside = input("Insert the inside local address: ")
						nat_list_outside = input("Insert inside global address: ")
						nat_list_translation = ("enable" "\n" "configure terminal" "\n" "ip nat inside source static " + str(nat_list_inside) + " " + str(nat_list_outside))
						return str(nat_ask), str(nat_list_translation)
				if nat_ask != str("pool"):
					print("please input 'pool' or 'translation'")
					natcreator()
				elif nat_ask != str("translation"):
					print("please input 'pool' or 'translation'")
					natcreator()
			except (ValueError, TypeError, AttributeError):
				print("Invalid inputs, try again ")
				aclcreator()

	if userinput == ("nat"):	
			nat = natcreator()
			if nat[0] == str("pool"):
				nat = str(nat[1])
				print(nat)
			elif nat[0] == str("translation"):
				nat = str(nat[1])
				print(nat)
			
	def dhcpcreator():
			try:
				dhcp_pool_name = input("Input the name for the dhcp pool: ")
				dhcp_default_route = input("Input the default router IP: ")
				dhcp_dns = input("Input the name server address: ")
				dns_network = input("Input the subnet IP: ")
				dns_network_mask = input("Input the subnet mask: ")
				dhcp_total = ("\n" "enable" "\n" "configure terminal" "\n" "ip dhcp pool " + str(dhcp_pool_name) + "\n" "default-router " + str(dhcp_default_route) + "\n" + "dns-server " + str(dhcp_dns) + "\n" "network " + str(dns_network) + " " + str(dns_network_mask))
				return str(dhcp_total)
			except (ValueError, TypeError, AttributeError):
				print("Invalid inputs, try again ")
				dhcpcreator()

	if userinput == ("dhcp"):	
			dhcp = dhcpcreator()
			print(dhcp)

	if userinput == ("help"):		
		helptext = ("\n" "The commands include: ospf, ip, stp, vlans, password, port security, cdp, rip, speed, duplex, portfast, acl, nat, dhcp " "\n")
		print(helptext)
		main()

	if userinput != list[str("ospf"), str("ip"), str("stp"), str("vlan"), str("passwords"), str("port security"), str("cdp"), str("rip"), str("speed"), str("duplex"), str("portfast"), str("acl"), str("nat"), str("dhcp")]:
		if True:
			restart()
	
	restart()	

main()
