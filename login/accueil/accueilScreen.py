from kivymd.uix.screen import MDScreen

class AccueilSc(MDScreen):
    def chater(self):
        self.manager.current = "go_chat"
    def preface(self):
        self.manager.current = "pref"
    def on_enter(self, *args):
        pass