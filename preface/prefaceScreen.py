from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import SlideTransition

class PreSc(MDScreen):
    def retour_page_precedente(self):
        self.manager.transition = SlideTransition()
        self.manager.current = "enter"
    def on_enter(self):
        pass
    