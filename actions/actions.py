# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset, SlotSet

class ActionAskEmail(Action):
    def name(self) -> Text:
        return "action_ask_email"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        if tracker.get_slot("previous_email"):
            dispatcher.utter_message(response=f"utter_ask_use_previous_email",)
        else:
            dispatcher.utter_message(response=f"utter_ask_email")
        return []
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_open_incident"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        email = tracker.get_slot("email")
        problem_description = tracker.get_slot("problem_description")
        incident_title = tracker.get_slot("content_type")
        confirm = tracker.get_slot("confirm")
        if not confirm:
            dispatcher.utter_message(
                response="utter_incident_creation_canceled"
            )
            return [AllSlotsReset(), SlotSet("previous_email", email)]
        else:
            message = (
                f"An incident with the following details would be opened\n"
                f"email: {email}\n"
                f"problem description: {problem_description}\n"
                f"title: {incident_title}"
                f"message: ticket has been created successfully")
            dispatcher.utter_message(message)
            return [AllSlotsReset(), SlotSet("previous_email", email)]
