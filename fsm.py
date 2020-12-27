from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
        self.command = ""
        self.dep = ""
        self.course = ""

    def is_going_to_help(self, event):
        text = event.message.text
        return text.lower() == "help"
    
    def is_going_to_state1_dep(self, event):
        text = event.message.text
        return text == "1" or text == "2" text == "3"

    def on_enter_help(silf, event):
        replay_message = ("查詢課程大綱請按1\n"+
                          "查詢課程餘額請按2\n"+
                          "查詢課程教室請按3")
        reply_token = event.reply_token
        send_text_message(reply_token, replay_message)

    def on_enter_dep(silf, event):
        self.command = event.message.text
        replay_message = "請輸入系所序號"
        reply_token = event.reply_token
        send_text_message(reply_token, replay_message)

    def on_enter_course(silf, event):
        self.dep = event.message.text
        replay_message = "請輸入系所課程"
        reply_token = event.reply_token
        send_text_message(reply_token, replay_message)

    def on_enter_print(silf, event):
        self.course = event.message.text
        command_text = ""
        if self.command == "1"
            command_text = "查詢課程大綱"
        elif self.command == "2"
            command_text = "查詢課程餘額"
        else
            command_text = "查詢課程教室"
        replay_message = ("command: " + command_text + "\n" +
                          "系所序號: " +  self.dep + "\n" + 
                          "系所課程: " + self.course)
        reply_token = event.reply_token
        send_text_message(reply_token, replay_message)