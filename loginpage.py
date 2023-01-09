from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty


Window.size = (360, 640)


class LoginPge(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginPge, self).__init__()

    def on_info_click(self, btn):
        pass
    
    def on_signin_press(self, btn):
        btn.background_color = (0, 0, 0, .3)
        
    def on_signin_release(self, btn):
        btn.background_color = (0, 0, 0, 0)


class LoginScreenApp(App):
    def build(self):
        return LoginPge()


LoginScreenApp().run()
