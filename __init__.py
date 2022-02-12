from mycroft import MycroftSkill, intent_file_handler


class BasicSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('skill.basic.intent')
    def handle_skill_basic(self, message):
        self.speak_dialog('skill.basic')


def create_skill():
    return BasicSkill()

