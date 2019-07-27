# -*- coding: utf-8 -*-
from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class accountForm(FormAction):
    

    def name(self) -> Text:
        # unique form name for account opening
        return "account_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        # list of all the fields from readme.

        return ["account_name", "industry", "turnover", "employee_no"]

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        # utter submit template
        dispatcher.utter_template("utter_submit", tracker)
        return []