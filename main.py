import json, glob, random
from datetime import datetime
from pathlib import Path
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from hoverable import HoverBehavior

Builder.load_file('design.kv')

class LoginScreen(Screen):
    # def __init__(self):
    #     self.ids.username.text="user1"
    #     self.ids.password.text="password1"

    def sign_up(self):        
        self.manager.current = "signup_screen"
    
    def login(self, uname, pword):
        with open("./data/users.json") as file:
            users = json.load(file)
        if uname in users and users[uname]["password"] == pword:
            self.manager.current = "login_success_screen"
        else:
            self.ids.msg.text = "Wrong username or password!"      

class LoginSuccessScreen(Screen):
    def log_out(self):
        self.manager.transition.direction="right"
        self.manager.current="login_screen"
    
    def enlighten_me(self, feeling):
        feeling = feeling.lower()
        file_list = glob.glob("./data/*.txt")
        avail_feeling = [Path(filename).stem for filename in file_list]
        if feeling in avail_feeling:
            with open(f"./data/{feeling}.txt", encoding="utf-8") as file:
                quotes = file.readlines()
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = "Try another feeling"

class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        with open("./data/users.json") as file:
            users = json.load(file)
        
        users[uname] = {"username": uname,
                        "password": pword,
                        "created_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        
        with open("./data/users.json", "w") as file:
            json.dump(users, file)
        
        self.manager.current="signup_success_screen"

class SignUpSuccessScreen(Screen):
    def change_login(self):
        self.manager.transition.direction="right"
        self.manager.current="login_screen"

class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__=="__main__":
    MainApp().run()