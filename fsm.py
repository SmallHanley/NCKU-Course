from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
        self.command = 0
        self.dep = ""
        self.course = ""

    def is_going_to_help(self, event):
        text = event.message.text
        return text.lower() == "help"
    
    def is_going_to_state1_dep(self, event):
        text = event.message.text
        return text.lower() == "1"

    def on_enter_help(silf, event):
        replay_message = "查詢課程大綱請按1\n"+
                         "查詢課程餘額請按2\n"+
                         "查詢課程教室請按3"
        reply_token = event.reply_token
        send_text_message(reply_token, replay_message)

    def on_enter_state1_dep(silf, event):
        replay_message = "請輸入系所序號"
        reply_token = event.reply_token
        send_text_message(reply_token, replay_message)

    def on_enter_state1_course(silf, event):
        text = event.message.text
        replay_message = "請輸入系所課程" + text.lower()
        reply_token = event.reply_token
        send_text_message(reply_token, replay_message)