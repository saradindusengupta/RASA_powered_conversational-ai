from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import yaml
from rasa_core.utils import EndpointConfig


nlu_interpreter = RasaNLUInterpreter('/home/saradindu/dev/Work-II/Happsales/models/nlu/default/happsales')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load('/home/saradindu/dev/Work-II/Happsales/models/dialogue', interpreter = nlu_interpreter, action_endpoint = action_endpoint)

input_channel = SlackInput('xoxb-689270623414-686663702964-75Dyj62bKpzoJ2fhZ2d0ePdl')

agent.handle_channels([input_channel], 5005, serve_forever=True)