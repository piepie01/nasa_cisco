import telnetlib
import time
import sys


def showArp(tn):
	s = 'show arp'
	tn.write(s.encode('ascii')+b"\n")
	time.sleep(1)
	print (tn.read_very_eager().decode('ascii'))
def exit(tn):
	s = 'exit'
	tn.write(s.encode('ascii')+b"\n")
def deleteSwitch(s):
	temp_list = s.split('\n')
	str_out = ''
	for element in temp_list:
		print (element.find("Switch"))
		if element.find("Switch") == -1:
			str_out = str_out + element
			str_out = str_out + '\n'
	return str_out

