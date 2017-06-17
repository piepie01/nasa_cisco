import telnetlib
import time
import sys


def showArp(tn,SwitchName):
	s = 'show arp'
	tn.write(s.encode('ascii')+b"\n")
	time.sleep(1)
	output = tn.read_very_eager().decode('ascii')
	output = delete(output,s)
	output = delete(output,SwitchName)
	print (output)
def exit(tn):
	s = 'exit'
	tn.write(s.encode('ascii')+b"\n")
def showrun(tn,password,SwitchName):
	list_s = ['show ru','disable']
	enable(tn,password)
	tn.write(list_s[0].encode('ascii')+b"\n")
	time.sleep(1)
	tn.write(list_s[1].encode('ascii')+b"\n")
	output = tn.read_very_eager().decode('ascii')
	output = delete(output,SwitchName + '>')
	output = delete(output,SwitchName + '#')
	print (output)
def showintstat(tn,password,SwitchName):
	list_s = ['show interface status','disable']
	enable(tn,password)
	tn.write(list_s[0].encode('ascii')+b"\n")
	time.sleep(1)
	tn.write(list_s[1].encode('ascii')+b"\n")
	output = tn.read_very_eager().decode('ascii')
	output = delete(output,SwitchName)
	print (output)

def showint(tn,password,SwitchName):
	list_s = ['show interface','disable']
	enable(tn,password)
	tn.write(list_s[0].encode('ascii')+b"\n")
	time.sleep(1)
	tn.write(list_s[1].encode('ascii')+b"\n")
	output = tn.read_very_eager().decode('ascii')
	output = delete(output,SwitchName)
	print (output)
def showportchannel(tn,password,SwitchName):
	list_s = ['show etherchannel port-channel','disable']
	enable(tn,password)
	tn.write(list_s[0].encode('ascii')+b"\n")
	time.sleep(1)
	tn.write(list_s[1].encode('ascii')+b"\n")
	output = tn.read_very_eager().decode('ascii')
	output = delete(output,SwitchName)
	print (output)
def showvlan(tn,password,SwitchName):
	list_s = ['show vlan','disable']
	enable(tn,password)
	tn.write(list_s[0].encode('ascii')+b"\n")
	time.sleep(1)
	tn.write(list_s[1].encode('ascii')+b"\n")
	output = tn.read_very_eager().decode('ascii')
	output = delete(output,SwitchName)
	print (output)
def showvlanid(tn,password,SwitchName):
	list_s = ['show vlan id ','disable']
	vlan_id = input("ID(1-4094):")
	list_s[0] = list_s[0] + vlan_id
	enable(tn,password)
	tn.write(list_s[0].encode('ascii')+b"\n")
	time.sleep(1)
	tn.write(list_s[1].encode('ascii')+b"\n")
	output = tn.read_very_eager().decode('ascii')
	output = delete(output,SwitchName)
	print (output)
def showmac(tn,password,SwitchName):
	list_s = ['show mac address-table','disable']
	enable(tn,password)
	tn.write(list_s[0].encode('ascii')+b"\n")
	time.sleep(1)
	tn.write(list_s[1].encode('ascii')+b"\n")
	output = tn.read_very_eager().decode('ascii')
	output = delete(output,SwitchName)
	print (output)
def setinfo(tn,password,ChangeName):
	list_s = ['config term','hostname ','exit','disable']
	enable(tn,password)
	tn.write(list_s[0].encode('ascii')+b"\n")
	tn.write(list_s[1].encode('ascii')+ChangeName.encode('ascii')+b"\n")
	tn.write(list_s[2].encode('ascii')+b"\n")
	tn.write(list_s[3].encode('ascii')+b"\n")
	time.sleep(1)
	tn.read_very_eager().decode('ascii')	
def settime(tn,password):
	list_s = ['clock set ','disable']
	hh = input('hour(0-23):')
	mm = input('minute(0-59):')
	ss = input('second(0-59):')
	day = input('day(1-31):')
	month = input('month(Jan-Dec):')
	year = input('year(1993-2035):')
	enable(tn,password)
	tn.write((list_s[0]+hh+':'+mm+':'+ss+' '+day+' '+month+' '+year+'\n').encode('ascii'))
	time.sleep(1)
	output = tn.read_very_eager().decode('ascii')
	if output.find('Unrecognized')!=-1 or output.find('Invalid')!=-1:
		print ("Invalid input")
	tn.write(list_s[1].encode('ascii')+b'\n')
	tn.read_very_eager().decode('ascii')	
def vlanadd(tn,password):
	list_s = ['config term','vlan ','exit','exit','disable']
	vlan_id = input("vlan id(1-4094):")
	if int(vlan_id) < 1 or int(vlan_id) > 4094:
		print ("Invalid id")
		return
	enable(tn,password)
	tn.write(list_s[0].encode('ascii')+b'\n')
	tn.write(list_s[1].encode('ascii')+vlan_id.encode('ascii')+b'\n')
	tn.write(list_s[2].encode('ascii')+b'\n')
	tn.write(list_s[3].encode('ascii')+b'\n')
	tn.write(list_s[4].encode('ascii')+b'\n')
	time.sleep(1)
	tn.read_very_eager().decode('ascii')	

def vlandel(tn,password):
	list_s = ['config term','no vlan ','exit','disable']
	vlan_id = input("vlan id(2-4094):")
	if int(vlan_id) < 2 or int(vlan_id) > 4094:
		print ("Invalid id")
		return
	enable(tn,password)
	tn.write(list_s[0].encode('ascii')+b'\n')
	tn.write(list_s[1].encode('ascii')+vlan_id.encode('ascii')+b'\n')
	tn.write(list_s[2].encode('ascii')+b'\n')
	tn.write(list_s[3].encode('ascii')+b'\n')
	time.sleep(1)
	tn.read_very_eager().decode('ascii')	
def vlanset(tn,password):
	list_s = ['config term','interface ','switchport mode access','switchport access vlan ','end','disable']
	interface = input("Interface:")
	vlan_id = input("vlan_id(1-4094):")
	if int(vlan_id) < 2 or int(vlan_id) > 4094:
		print ("Invallid id")
		return
	enable(tn,password)
	tn.write(list_s[0].encode('ascii')+b'\n')
	tn.write(list_s[1].encode('ascii')+interface.encode('ascii')+b'\n')
	time.sleep(0.5)
	output = tn.read_very_eager().decode('ascii')
	if output.find("Incomplete") != -1 or output.find("Invalid") != -1:
		print ("Invalid interface")
		tn.write(list_s[4].encode('ascii')+b'\n')
		tn.write(list_s[5].encode('ascii')+b'\n')
		return
	tn.write(list_s[2].encode('ascii')+b'\n')
	tn.write(list_s[3].encode('ascii')+vlan_id.encode('ascii')+b'\n')
	tn.write(list_s[4].encode('ascii')+b'\n')
	tn.write(list_s[5].encode('ascii')+b'\n')
	tn.read_very_eager().decode('ascii')
def delete(s,goal):
	temp_list = s.split('\n')
	str_out = ''
	for element in temp_list:
		if element.find(goal) == -1 and element != '\n':
			str_out = str_out + element
			str_out = str_out + '\n'
	return str_out
def enable(tn,password):
	tn.write("enable".encode('ascii')+b"\n")
	tn.read_until(b'Password:')
	tn.write(password.encode('ascii')+b'\n')
	
