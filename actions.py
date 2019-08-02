# -*- coding: utf-8 -*-
#from future import absolute_import
#from future import division
#from future import unicode_literals

from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class AccountForm(FormAction):
	

	def name(self) -> Text:
		# unique form name for account opening
		return "account_form"

	@staticmethod
	def required_slots(tracker: Tracker) -> List[Text]:
		# list of all the fields from readme.

		return ["accountname", "industry", "turnover", "employee_no"]
	
	def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

		return	{
	  		"accountname": [self.from_entity(entity="accountname", intent="inform")],
			"industry": [self.from_entity(entity="industry", intent=["inform"])],
			"turnover": [self.from_entity(entity="turnover"),self.from_intent(intent="inform", value=True)],
			"employee_no": [self.from_entity(entity="employee_no"),self.from_intent(intent="inform", value=True)]
				}    

	def submit(
		self,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any],
		) -> List[Dict]:

		# utter submit template
		dispatcher.utter_template("utter_submit", tracker)
		return []

class AccountForm_one(FormAction):
	

	def name(self) -> Text:
		# unique form name for account opening
		return "account_form_one"

	@staticmethod
	def required_slots(tracker: Tracker) -> List[Text]:
		# list of all the fields from readme.

		return ["contactname", "phone", "mobile", "email", "department", "designation"]
	
	def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

		return	{
	  		"contactname": [self.from_entity(entity="accountname", intent="inform")],
			"phone": [self.from_entity(entity="industry", intent=["inform"])],
			"mobile": [self.from_entity(entity="turnover")],
			"email": [self.from_entity(entity="employee_no")],
			"department": [self.from_entity(entity="employee_no")],
			"designation": [self.from_entity(entity="employee_no")]
				}    

	def submit(
		self,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any],
		) -> List[Dict]:

		# utter submit template
		dispatcher.utter_template("utter_submit", tracker)
		return []