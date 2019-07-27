from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter

def train_nlu(data, configs, model_dir):
	training_data = load_data(data)
	trainer = Trainer(config.load(configs))
	trainer.train(training_data)
	model_directory = trainer.persist(model_dir, fixed_model_name = 'happsales')
	
def run_nlu():
	interpreter = Interpreter.load('/home/saradindu/dev/Work-II/Happsales/models/nlu/default/happsales')
	#print(interpreter.parse(u"I am planning my holiday to Lithuania. I wonder what is the weather out there."))
	print(interpreter.parse(u"create a account"))	
if __name__ == '__main__':
	train_nlu('/home/saradindu/dev/Work-II/Happsales/data/data.json', 'config.yml', '/home/saradindu/dev/Work-II/Happsales/models/nlu/')
	run_nlu()
