# This is a skeleton for Err plugins, use this to get started quickly.

from errbot import BotPlugin, botcmd
from errbot.builtins.webserver import webhook
from datetime import datetime
import urllib

class evetime(BotPlugin):
	"""An Err plugin skeleton"""
	#min_err_version = '1.6.0' # Optional, but recommended
	#max_err_version = '2.0.0' # Optional, but recommended

	def activate(self):
		"""Triggers on plugin activation

		You should delete it if you're not using it to override any default behaviour"""
		super(evetime, self).activate()

	def deactivate(self):
		"""Triggers on plugin deactivation

		You should delete it if you're not using it to override any default behaviour"""
		super(evetime, self).deactivate()

	def get_configuration_template(self):
		"""Defines the configuration structure this plugin supports

		You should delete it if your plugin doesn't use any configuration like this"""
		return {'EXAMPLE_KEY_1': "Example value",
		        'EXAMPLE_KEY_2': ["Example", "Value"]
		       }

	def check_configuration(self, configuration):
		"""Triggers when the configuration is checked, shortly before activation

		You should delete it if you're not using it to override any default behaviour"""
		super(evetime, self).check_configuration()

	def callback_connect(self):
		"""Triggers when bot is connected

		You should delete it if you're not using it to override any default behaviour"""
		pass

	def callback_message(self, conn, message):
		"""Triggered for every received message that isn't coming from the bot itself

		You should delete it if you're not using it to override any default behaviour"""
		pass

	def callback_botmessage(self, message):
		"""Triggered for every message that comes from the bot itself

		You should delete it if you're not using it to override any default behaviour"""
		pass

	@webhook
	def example_webhook(self, incoming_request):
		"""A webhook which simply returns 'Example'"""
		return "Example"

	# Passing split_args_with=None will cause arguments to be split on any kind
	# of whitespace, just like Python's split() does
	@botcmd(split_args_with=None)
	def evetime(self, mess, args):
		"""Provides the current time in the Eve Online Universe"""
		time=datetime.utcnow().strftime('%H:%M')
		output="It is currently " + time + " EVE Time"
		return output
