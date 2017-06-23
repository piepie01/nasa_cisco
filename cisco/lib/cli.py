from pexpect import pxssh
import time
import sys
from getpass import getpass

def showArp(ssh,SwitchName):
	s = 'show arp'
	ssh.sendline(s)
	ssh.prompt(timeout = 1)
	output = ssh.before.decode('ascii')
	ssh.expect (r'.+')
	output = delete(output,s)
	output = delete(output,SwitchName+'#')
	print (output)
def showrun(ssh,password,SwitchName):
	s = 'show ru'
	ssh.sendline(s)
	ssh.prompt(timeout = 1)
	output = ssh.before.decode('ascii')
	ssh.expect (r'.+')
	output = delete(output,s)
	output = delete(output,SwitchName+'#')
	print (output)
def showintstat(ssh,password,SwitchName):
	s = 'show interface status'
	ssh.sendline(s)
	ssh.prompt(timeout = 1)
	output = ssh.before.decode('ascii')
	ssh.expect (r'.+')
	output = delete(output,s)
	output = delete(output,SwitchName+'#')
	print (output)

def showint(ssh,password,SwitchName):
	s = 'show interface'
	ssh.sendline(s)
	ssh.prompt(timeout = 1)
	output = ssh.before.decode('ascii')
	ssh.expect (r'.+')
	output = delete(output,s)
	output = delete(output,SwitchName+'#')
	print (output)
def showportchannel(ssh,password,SwitchName):
	s = 'show etherchannel port-channel'
	ssh.sendline(s)
	ssh.prompt(timeout = 1)
	output = ssh.before.decode('ascii')
	ssh.expect (r'.+')
	output = delete(output,s)
	output = delete(output,SwitchName+'#')
	print (output)
def showvlan(ssh,password,SwitchName):
	s = 'show vlan'
	ssh.sendline(s)
	ssh.prompt(timeout = 1)
	output = ssh.before.decode('ascii')
	ssh.expect (r'.+')
	output = delete(output,s)
	output = delete(output,SwitchName+'#')
	print (output)
def showvlanid(ssh,password,SwitchName):
	s = 'show vlan id '
	vlan_id = input("ID(1-4094):")
	s = s + vlan_id
	ssh.sendline(s)
	ssh.prompt(timeout = 1)
	output = ssh.before.decode('ascii')
	ssh.expect (r'.+')
	output = delete(output,s)
	output = delete(output,SwitchName+'#')
	print (output)
def showmac(ssh,password,SwitchName):
	s = 'show mac address-table'
	ssh.sendline(s)
	ssh.prompt(timeout = 1)
	output = ssh.before.decode('ascii')
	ssh.expect (r'.+')
	output = delete(output,s)
	output = delete(output,SwitchName+'#')
	print (output)
def setinfo(ssh,password,ChangeName):
	list_s = ['config term','hostname '+ChangeName,'exit']
	ssh.sendline(list_s[0])
	ssh.sendline(list_s[1])
	ssh.sendline(list_s[2])
	ssh.prompt(timeout = 1)
	ssh.expect (r'.+')
def settime(ssh,password):
	s = 'clock set '
	hh = input('hour(0-23):')
	mm = input('minute(0-59):')
	ss = input('second(0-59):')
	day = input('day(1-31):')
	month = input('month(Jan-Dec):')
	year = input('year(1993-2035):')
	ssh.sendline(s+hh+':'+mm+':'+ss+' '+day+' '+month+' '+year)
	ssh.prompt(timeout=1)
	if output.find('Unrecognized')!=-1 or output.find('Invalid')!=-1:
		print ("Invalid input")
	ssh.expect(r'.+')
def vlanadd(ssh,password):
	list_s = ['config term','vlan ','exit','exit']
	vlan_id = input("vlan id(1-4094):")
	if int(vlan_id) < 1 or int(vlan_id) > 4094:
		print ("Invalid id")
		return
	ssh.sendline(list_s[0])
	ssh.sendline(list_s[1]+vlan_id)
	ssh.sendline(list_s[2])
	ssh.sendline(list_s[3])
	ssh.prompt(timeout=1)
	ssh.expect(r'.+')
def vlandel(ssh,password):
	list_s = ['config term','no vlan ','exit']
	vlan_id = input("vlan id(2-4094):")
	if int(vlan_id) < 2 or int(vlan_id) > 4094:
		print ("Invalid id")
		return
	ssh.sendline(list_s[0])
	ssh.sendline(list_s[1]+vlan_id)
	ssh.sendline(list_s[2])
	ssh.prompt(timeout=1)
	ssh.expect(r'.+')
def vlanset(ssh,password):
	list_s = ['config term','interface ','switchport mode access','switchport access vlan ','end']
	interface = input("Interface:")
	vlan_id = input("vlan_id(1-4094):")
	if int(vlan_id) < 2 or int(vlan_id) > 4094:
		print ("Invalid id")
		return
	ssh.sendline(list_s[0])
	ssh.sendline(list_s[1]+interface)
	ssh.prompt(timeout=1)
	output = ssh.before.decode('ascii')
	if output.find("Incomplete") != -1 or output.find("Invalid") != -1:
		print ("Invalid interface")
		ssh.sendline(list_s[4])
		ssh.expect(r'.+')
		return
	ssh.sendline(list_s[2])
	ssh.sendline(list_s[3]+vlan_id)
	ssh.sendline(list_s[4])
	ssh.prompt(timeout=1)
	output = ssh.before.decode('ascii')
	print(output)
	ssh.expect(r'.+')
def trunk(ssh):
	interface = input("Interface:")
	vlan_id = input("vlan_id(1-4094):")
	if int(vlan_id) < 2 or int(vlan_id) > 4094:
		print ("Invalid id")
		return
	list_s = ['config t','interface Gi0/'+interface,'switchport mode trunk','switchport trunk allowed vlan add '+vlan_id,'end']
	ssh.sendline(list_s[0])
	ssh.sendline(list_s[1])
	ssh.prompt(timeout=1)
	output = ssh.before.decode('ascii')
	if output.find("Incomplete") != -1 or output.find("Invalid") != -1:
		print ("Invalid interface")
		ssh.sendline(list_s[4])
		ssh.expect(r'.+')
		return
	ssh.sendline(list_s[2])
	ssh.sendline(list_s[3])
	ssh.sendline(list_s[4])
	ssh.prompt(timeout=1)
	output = ssh.before.decode('ascii')
	print(output)
	ssh.expect(r'.+')
def setaccount(ssh,SwitchName):
	ChangeName = input("Username:")
	ChangePassword = getpass('Password:')
	list_s = ['sh ru | i user','configure term','username '+ChangeName+' priv 15 password '+ChangePassword,'no ','exit']
	ssh.sendline(list_s[0])
	ssh.prompt(timeout=1)
	user = ssh.before.decode('ascii')
	user = delete(user,'root')
	user = delete(user,list_s[0])
	user = delete(user,SwitchName)
	user = user.split('\n')[0]
	ssh.sendline(list_s[1])
	ssh.sendline(list_s[2])
	ssh.sendline(list_s[3]+user)
	ssh.sendline(list_s[4])
	ssh.prompt(timeout=1)
	ssh.expect(r'.+')
	ssh.logout()
def write(ssh):
	list_s = ['show boot','copy system:running-config ']
	ssh.sendline(list_s[0])
	ssh.prompt(timeout=1)
	fileName = ssh.before.decode('ascii')
	list_file = fileName.split('\n')
	for element in list_file:
		if element.find('Config file') != -1:
			fileName = element[22:]
			break
	#print (fileName)
	list_s[1]=list_s[1]+fileName
	ssh.sendline(list_s[1])
	ssh.sendline('')
	ssh.sendline('')
	ssh.prompt(timeout=1)
	output = ssh.before.decode('ascii')
	ssh.expect(r'.+')
def ping(ssh, ipAddr, count, interval, size, SwitchName):
	list_s = ['ping ip '+ipAddr+' repeat '+count+' timeout '+interval+' size '+size]
	ssh.sendline(list_s[0])
	ssh.prompt(timeout=1)
	output = ssh.before.decode('ascii')
	output = delete(output,list_s[0])
	output = delete(output,SwitchName)
	print (output)
	ssh.expect(r'.+')
def delete(s,goal):
	temp_list = s.split('\n')
	str_out = ''
	for element in temp_list:
		if element.find(goal) == -1 and element != '\n':
			str_out = str_out + element
			str_out = str_out + '\n'
	return str_out
def getSwitchName(ssh):
	s = 'show ru'
	ssh.sendline(s)
	ssh.prompt(timeout = 1)
	output = ssh.before.decode('ascii')
	ssh.expect (r'.+')
	temp_list = output.split('\n')
	switchname=''
	for element in temp_list:
		if element.find('hostname') != -1:
			switchname = element[9:]
			break
	return switchname[:len(switchname)-1]
def setportchannel(ssh):
	interfacerange_start = input("Configure interface from:")
	interfacerange_end = input("to:")
	channel = input("Assign the ports to a channel group (For channel group number, the range is 1 to 6):")
	list_s = ['config t','interface range Gi0/'+interfacerange_start+'-'+interfacerange_end, 'channel-group '+channel+' mode active','end']
	ssh.sendline(list_s[0])
	ssh.sendline(list_s[1])
	ssh.sendline(list_s[2])
	ssh.sendline(list_s[3])
	ssh.prompt(timeout=1)
	output = ssh.before.decode('ascii')
	print(output)
	ssh.expect(r'.+')
def clearportchannel(ssh):
	channel = input("Enter port channel number:")
	list_s = ['config t','no interface Port-channel '+channel, 'exit']
	ssh.sendline(list_s[0])
	ssh.sendline(list_s[1])
	ssh.sendline(list_s[2])
	ssh.prompt(timeout=1)
	output = ssh.before.decode('ascii')
	if 'Invalid' in output:
		print ("Invalid port channel")
	#print(output)
	ssh.expect(r'.+')
def setportstatus(ssh,mode):
	interface = input("Enter the port number: ")
	list_s = ['config t','interface Gi0/'+interface,'shutdown','no shutdown','end']
	ssh.sendline(list_s[0])
	ssh.sendline(list_s[1])
	if mode == "d" :
		ssh.sendline(list_s[2])
	if mode == "e" :
		ssh.sendline(list_s[3])
	ssh.sendline(list_s[4])
	ssh.prompt(timeout=1)
	output = ssh.before.decode('ascii')
	#print(output)
	ssh.expect(r'.+')
def uploadconfig(ssh):
	username = input("Username:")
	password = getpass("Password:")
	host = input("Host:")
	filename = input("Filename:")
	if filename[:1] != '/':
		filename = '/' + filename
	list_s = ['copy ftp://'+username+':'+password+'@'+host+filename+' system:running-config','']
	ssh.sendline(list_s[0])
	ssh.sendline(list_s[1])
	ssh.prompt(timeout=1)
	output = ssh.before.decode('ascii')
	print(output)
	ssh.expect(r'.+')
def downloadconfig(ssh):
	username = input("Username:")
	password = getpass("Password:")
	host = input("Host:")
	filename = input("Filename:")
	if filename[:1] != '/':
		filename = '/' + filename
	list_s = ['copy system:running-config ftp://'+username+':'+password+'@'+host+filename,'']
	ssh.sendline(list_s[0])
	ssh.sendline(list_s[1])
	ssh.prompt(timeout=1)
	output = ssh.before.decode('ascii')
	print(output)
	ssh.expect(r'.+')
