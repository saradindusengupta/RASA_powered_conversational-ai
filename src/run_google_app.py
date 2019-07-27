from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from google_connecter import GoogleConnector
from rasa_core.utils import EndpointConfig

action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
nlu_interpreter = RasaNLUInterpreter('/home/saradindu/dev/Work-II/Happsales/models/nlu/default/happsales')
agent = Agent.load('/home/saradindu/dev/Work-II/Happsales/models/dialogue', interpreter = nlu_interpreter, action_endpoint=action_endpoint)

input_channel = GoogleConnector()
agent.handle_channels([input_channel], 5005, serve_forever=True)