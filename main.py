from kivy.uix.screenmanager import ScreenManager, NoTransition
#from kivymd.uix.label import MDLabel 
#from kivy.core.window import Wigndow
#from kivy.lang import Builder
from kivymd.app import MDApp
from kivy import Config
#from kivymd.uix.boxlayout import MDBoxLayout

#Window.size= (300, 600)

Config.set('kivy', 'exit_on_escape', '0')


class WindowManager(ScreenManager):
    def route_initial(self):
        self.transition=NoTransition()
        self.current ="first"
        
    
class MainApp(MDApp):
    def build(self):
        manager= WindowManager()
        manager.route_initial()
        return manager
        # retur, Builder.load_file('main.kv)
        
app = MainApp()
app.run()