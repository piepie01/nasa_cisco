import telnetlib
import time
from getpass import getpass
import sys
from cmd import Cmd
from lib import cli

class Prompt(Cmd):
	def do_showarp(self, args):
		cli.showArp(tn,SwitchName)
	def do_forceexit(self, args):
		"""Quit the program without logout."""
		raise SystemExit

	def do_EOF(self, args):
		"""Logout current switch and exit."""
		cli.exit(tn)
		raise SystemExit

	def do_exit(self, args):
		"""Logout current switch and exit."""
		cli.exit(tn)
		raise SystemExit

	def do_showrun(self, args):
		"""Show switch dashboard information."""
		cli.showrun(tn,password,SwitchName)

	def do_showintstat(self, args):
		"""Show port packet statistics."""
		cli.showintstat(tn,password,SwitchName)

	def do_showint(self, args):
		"""Show interfaces status."""
		cli.showint(tn,password,SwitchName)

	def do_showportchannel(self, args):
		"""Show port channel information."""
		cli.showportchannel(tn,password,SwitchName)

	def do_showvlan(self, args):
		"""Show interface VLAN membership."""
		cli.showvlan(tn,password,SwitchName)

	def do_showvlanid(self, args):
		"""Show VLAN id status."""
		cli.showvlanid(tn,password,SwitchName)

	def do_showmac(self, args):
		"""Show mac address table."""
		cli.showmac(tn,password,SwitchName)

	def do_setinfo(self, args):
		"""Set switch name, Location, contact."""
		global SwitchName
		ChangeName = input("Switch name:")
		cli.setinfo(tn,password,ChangeName)
		prompt.prompt = ChangeName + '>'
		SwitchName = ChangeName
	def do_write(args):
		"""Save configuration."""

	def do_setaccount(args):
		"""Modify administrative account."""
		user, cur_pwd, new_pwd, confirm_pwd = input("New username: "), getpass("Current password: "), getpass("New password: "), getpass("Retype new password: ")
		if new_pwd != confirm_pwd:
			print("Confirm password is different.")

	def do_setnetwork(args):
		"""Set switch IP, subnet, gateway, management vlan."""
		manage_vlan_id = input("management vlan id? (empty = 1)")
		manage_vlan_id = '1' if manage_vlan_id == '' else manage_vlan_id
		mode = input("dhcp or static?")
		while mode != "static" and mode != "dhcp":
			mode = input("dhcp or static?")

	def do_settime(self, args):
		"""Set SNTP server IP and timezone (support GMT+8 TPE only)."""
		cli.settime(tn,password)

	def do_vlanadd(self, args):
		"""Add a new vlan interface."""
		cli.vlanadd(tn,password)

	def do_vlandel(self, args):
		"""Delete a new vlan interface."""
		cli.vlandel(tn,password)

	def do_vlanset(self, args):
		"""Set interfaces vlan membership."""
		cli.vlanset(tn,password)

	def do_gencert(args):
		"""Generate a new self-signed SSL certificate."""
		print("Generating a new cert...")

	def do_sethttps(args):
		"""Set management connection protocal (HTTP or HTTPS)."""
		print("Note: If the new protocal is different from current one, you have to login again.")
		available_choice = {'http': ('enabled', 'disabled'), 'https':('disabled', 'enabled'), 'both':('enabled', 'enabled')}
		choice = input("http only[http]/https only[https]/both[both]?")
		while choice not in available_choice:
			choice = input("http only[http]/https only[https]/both[both]?")

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

	def do_ping(args):
		"""Ping an IP through the switch"""
		ipAddr, count, interval, size = input("IP address: "), input("Count (1-15): "), input("Interval (1-60 Seconds): "), input("Size (0-13000Bytes): ")

	def do_loopprotection(args):
		"""loop protection on all interface"""

	def do_setmgmtvlan(args):
		"""change management vlan id"""
		vlan_id = input("Vlan ID?: ")
prompt = Prompt()
tn = None
password = ''
SwitchName = ''
def run(_tn,_password,_SwitchName):
	global tn
	global password
	global SwitchName
	tn = _tn
	password = _password
	SwitchName = _SwitchName
	prompt.prompt = SwitchName + '>'
	while True:
		try:
			prompt.cmdloop("Type exit/forceexit to quit, help for help.")
		except KeyboardInterrupt:
			pass
