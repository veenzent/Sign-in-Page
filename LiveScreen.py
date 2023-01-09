from kaki.app import App
from kivy.factory import Factory
# from kivy.core.window import Window
import os

# Window.size = (360, 640)


class LoginLive(App):
    CLASSES = {
        "LoginPge": "loginpage"
    }

    KV_FILES = [os.path.join(os.getcwd(), "loginscreenApp.kv")]

    AUTORELOADER_PATHS = [
        (os.getcwd(), {"recursive": True})
    ]

    def build_app(self, first=False):
        # self.theme_cls.primary_palette = "Green"
        print("App Autoreloaded")
        return Factory.LoginPge()


LoginLive().run()
