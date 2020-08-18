from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from datetime import datetime
import json

Builder.load_file("design.kv")


class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"


class RootWidget(ScreenManager):
    pass


class SignUpScreen(Screen):
    def add_user(self, uname, passwd):
        with open("users.json") as file:
            users = json.load(file)
        users[uname] = {'username': uname, 'password': passwd, 'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}

        with open("users.json",'w') as file:
            json.dump(users, file)

class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    #print()
    app = MainApp()
    app.run()
    
