from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import rasa_core
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig
from rasa_core.run import serve_application

def run_happsales_bot(serve_forever=True):
	interpreter = RasaNLUInterpreter('/home/saradindu/dev/Work-II/Happsales/models/nlu/default/happsales')
	action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
	agent = Agent.load('/home/saradindu/dev/Work-II/Happsales/models/dialogue', interpreter=interpreter, action_endpoint=action_endpoint)
	rasa_core.run.serve_application(agent ,channel='cmdline')
		
	return agent

if __name__ == '__main__':
	run_happsales_bot()