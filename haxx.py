# Haxx Plugin for B3
# By clearskies (Anthony Nguyen)
# GPL licensed

import b3
import b3.plugin

__version__ = "2"
__author__ = "clearskies (Anthony Nguyen)"

class HaxxPlugin(b3.plugin.Plugin):
	requiresConfigFile = False

	def onStartup(self):
		self._admin = self.console.getPlugin("admin")
		self._admin.registerCommand(self, "aimbot", 2, self.cmd_aimbot, "aim")
		self._admin.registerCommand(self, "wallhack", 2, self.cmd_wallhack, "wh")
		self._admin.registerCommand(self, "poop", 2, self.cmd_poop, "poo")
		self._admin.registerCommand(self, "ragequit", 0, self.cmd_ragequit, "rq")

	def onEvent(self, event):
		pass

	def cmd_aimbot(self, data, client, cmd = None):
		if data == "on":
			self.console.say(client.exactName + " has ^5activated ^7his/her ^1AIMBOT!")
		elif data == "off":
			self.console.say(client.exactName + " has ^5deactivated ^7his/her ^1AIMBOT!")

	def cmd_wallhack(self, data, client, cmd = None):
		if data == "on":
			self.console.say(client.exactName + " has ^5activated ^7his/her ^1WALLHACKS!")
		elif data == "off":
			self.console.say(client.exactName + " has ^5deactivated ^7his/her ^1WALLHACKS!")

	def cmd_poop(self, data, client, cmd = None):
		if data:
			input = self._admin.parseUserCmd(data)
		if not data:
			self.console.write("bigtext \" {0} pooped!\"".format(client.exactName))
			return
		poopOn = self._admin.findClientPrompt(input[0], client)
		if poopOn:
			self.console.write("bigtext \" {0} pooped on {1}!\"".format(client.exactName, poopOn.exactName))


	def cmd_ragequit(self, data, client, cmd = None):
		client.kick()
		self.console.say(client.exactName + " ragequit like a baby!")

if __name__ == "__main__":
	from b3.fake import fakeConsole, superadmin
	plugin = HaxxPlugin(fakeConsole)
	plugin.onStartup()
	superadmin.connects(cid = 0)
	superadmin.says("!wh on")
