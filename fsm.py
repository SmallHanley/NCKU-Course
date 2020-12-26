from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_help(self, event):
        text = event.message.text
        return text.lower() == "help"

    def on_enter_help(silf, event):
        replay_message = "help"
        reply_token = event.reply_token
        send_text_message(reply_token, replay_message)