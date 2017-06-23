from pexpect import pxssh
import time
from getpass import getpass
import sys
from cmd import Cmd
from lib import cli

class Prompt(Cmd):
	def do_showarp(self, args):
		cli.showArp(ssh,SwitchName)
	def do_forceexit(self, args):
		"""Quit the program without logout."""
		raise SystemExit

	def do_EOF(self, args):
		"""Logout current switch and exit."""
		ssh.logout()
		raise SystemExit

	def do_exit(self, args):
		"""Logout current switch and exit."""
		ssh.logout()
		raise SystemExit

	def do_showrun(self, args):
		"""Show switch dashboard information."""
		cli.showrun(ssh,password,SwitchName)

	def do_showintstat(self, args):
		"""Show port packet statistics."""
		cli.showintstat(ssh,password,SwitchName)

	def do_showint(self, args):
		"""Show interfaces status."""
		cli.showint(ssh,password,SwitchName)

	def do_showportchannel(self, args):
		"""Show port channel information."""
		cli.showportchannel(ssh,password,SwitchName)

	def do_showvlan(self, args):
		"""Show interface VLAN membership."""
		cli.showvlan(ssh,password,SwitchName)

	def do_showvlanid(self, args):
		"""Show VLAN id status."""
		cli.showvlanid(ssh,password,SwitchName)

	def do_showmac(self, args):
		"""Show mac address table."""
		cli.showmac(ssh,password,SwitchName)

	def do_setinfo(self, args):
		"""Set switch name, Location, contact."""
		global SwitchName
		ChangeName = input("Switch name:")
		cli.setinfo(ssh,password,ChangeName)
		prompt.prompt = ChangeName + '>'
		SwitchName = ChangeName
	def do_write(self, args):
		"""Save configuration."""
		cli.write(ssh)

	def do_setaccount(self, args):
		"""Modify administrative account."""
		cli.setaccount(ssh,SwitchName)
		print ("login again")
		raise SystemExit

	def do_setnetwork(args):
		"""Set switch IP, subnet, gateway, management vlan."""
		manage_vlan_id = input("management vlan id? (empty = 1)")
		manage_vlan_id = '1' if manage_vlan_id == '' else manage_vlan_id
		mode = input("dhcp or static?")
		while mode != "static" and mode != "dhcp":
			mode = input("dhcp or static?")

	def do_settime(self, args):
		"""Set SNTP server IP and timezone (support GMT+8 TPE only)."""
		cli.settime(ssh,password)

	def do_vlanadd(self, args):
		"""Add a new vlan interface."""
		cli.vlanadd(ssh,password)

	def do_vlandel(self, args):
		"""Delete a new vlan interface."""
		cli.vlandel(ssh,password)

	def do_vlanset(self, args):
		"""Set interfaces vlan membership."""
		cli.vlanset(ssh,password)

	def do_gencert(args):
		"""Generate a new self-signed SSL certificate."""
		print("Generating a new cert...")

	def do_reset(args):
		"""Restore to factory configuration."""
		print("Note: After resetting, you have to save configuration to apply factory default when rebooting.")
		choice = input("Restore to factory configuration?(y/n)")
		while choice not in "yn":
			choice = input("Restore to factory configuration?(y/n)")
		if choice == 'y':
			nothing = 1
	def do_uploadconfig(args):
		"""Upload a config file to switch."""

	def do_uploadcode(args):
		"""Upload a firmware file to switch."""

	def do_activatecode(args):
		"""Activate the backup firmware code"""

	def do_downloadconfig(args):
		"""Download a config file to local."""

	def do_setportchannel(args):
		"""Configure port channel settings."""
		available_mode = {'y':'enabled', 'n':'disabled'}
		stp_mode = input("stp_mode (y/n)?")
		while stp_mode not in available_mode:
			stp_mode = input("stp_mode (y/n)?")
		static_mode = input("static_mode (y/n)?")
		while static_mode not in available_mode:
			static_mode = input("static_mode (y/n)?")

	def do_clearportchannel(args):
		"""Clear port channel settings."""

	def do_setportstatus(args):
		"""Enable or disable ports."""
		available_mode = {'e':'enabled', 'd':'disabled'}
		mode = input("enable or disable a port(e/d)?")
		while mode not in available_mode:
			mode = input("enable or disable a port(e/d)?")

	def do_ping(self, args):
		"""Ping an IP through the switch"""
		ipAddr, count, interval, size = input("IP address: "), input("Count (1-15): "), input("Interval (1-60 Seconds): "), input("Size (40-1000Bytes): ")
		cli.ping(ssh, ipAddr, count, interval, size, SwitchName)

	def do_loopprotection(args):
		"""loop protection on all interface"""

	def do_setmgmtvlan(args):
		"""change management vlan id"""
		vlan_id = input("Vlan ID?: ")
prompt = Prompt()
ssh = None
password = ''
SwitchName = ''
def run(_ssh,_password,_SwitchName):
	global ssh
	global password
	global SwitchName
	ssh = _ssh
	password = _password
	SwitchName = _SwitchName
	prompt.prompt = SwitchName + '>'
	print (prompt.prompt)
	while True:
		try:
			prompt.cmdloop("Type exit/forceexit to quit, help for help.")
		except KeyboardInterrupt:
			pass
