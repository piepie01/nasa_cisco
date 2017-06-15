import telnetlib
import time
import sys


def showArp(tn):
	s = 'show arp'
	tn.write(s.encode('ascii')+b"\n")
	time.sleep(1)
	output = tn.read_very_eager().decode('ascii')
	output = delete(output,s)
	output = delete(output,"Switch")
	print (output)
def exit(tn):
	s = 'exit'
	tn.write(s.encode('ascii')+b"\n")
def showrun(tn,password):
	list_s = ['show ru','disable']
	enable(tn,password)
	tn.write(list_s[0].encode('ascii')+b"\n")
	time.sleep(1)
	tn.write(list_s[1].encode('ascii')+b"\n")
	output = tn.read_very_eager().decode('ascii')
	output = delete(output,"Switch")
	print (output)
def showintstat(tn,password):
	list_s = ['show interface status','disable']
	enable(tn,password)
	tn.write(list_s[0].encode('ascii')+b"\n")
	time.sleep(1)
	tn.write(list_s[1].encode('ascii')+b"\n")
	output = tn.read_very_eager().decode('ascii')
	output = delete(output,"Switch")
	print (output)

def showint(tn,password):
	list_s = ['show interface','disable']
	enable(tn,password)
	tn.write(list_s[0].encode('ascii')+b"\n")
	time.sleep(1)
	tn.write(list_s[1].encode('ascii')+b"\n")
	output = tn.read_very_eager().decode('ascii')
	output = delete(output,"Switch")
	print (output)
def showportchannel(tn,password):
	list_s = ['show etherchannel port-channel','disable']
	enable(tn,password)
	tn.write(list_s[0].encode('ascii')+b"\n")
	time.sleep(1)
	tn.write(list_s[1].encode('ascii')+b"\n")
	output = tn.read_very_eager().decode('ascii')
	output = delete(output,"Switch")
	print (output)
def showvlan(tn,password):
	list_s = ['show vlan','disable']
	enable(tn,password)
	tn.write(list_s[0].encode('ascii')+b"\n")
	time.sleep(1)
	tn.write(list_s[1].encode('ascii')+b"\n")
	output = tn.read_very_eager().decode('ascii')
	output = delete(output,"Switch")
	print (output)
def showvlanid(tn,password):
	list_s = ['show vlan id ','disable']
	vlan_id = input("ID(1-4094):")
	list_s[0] = list_s[0] + vlan_id
	enable(tn,password)
	tn.write(list_s[0].encode('ascii')+b"\n")
	time.sleep(1)
	tn.write(list_s[1].encode('ascii')+b"\n")
	output = tn.read_very_eager().decode('ascii')
	output = delete(output,"Switch")
	print (output)
def showmac(tn,password):
	list_s = ['show mac address-table','disable']
	enable(tn,password)
	tn.write(list_s[0].encode('ascii')+b"\n")
	time.sleep(1)
	tn.write(list_s[1].encode('ascii')+b"\n")
	output = tn.read_very_eager().decode('ascii')
	output = delete(output,"Switch")
	print (output)
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
	
