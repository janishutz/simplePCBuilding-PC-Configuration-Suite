# This is the main runtime of the simplePCBuilding-PC-Configurator
# IMPORTS
import time
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.popup import Popup
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import mainthread
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock

version = "alpha 1.0"
print(f"Launching the simplePCBuilding-PC-Configurator Version {version}!...\nthis might take some time...")


###########
# SCREENS
###########


class Splash(MDScreen):
    pass


class Home(MDScreen):
    def test(self):
        print("class")


class ConfigureScreen(MDScreen):
    pass


#################
# SCREEN-MANAGER
#################


class PCConfigurator(MDApp):
    global screen_manager
    screen_manager = ScreenManager()
    def build(self):
        self.title = "simplePCBuilding-PC-Configurator"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "BlueGray"
        # self.icon = "./BiogasControllerAppLogo.png"
        screen_manager.add_widget(Builder.load_file("./gui_main/splashscreen.kv"))
        screen_manager.add_widget(Builder.load_file("./gui_main/main-gui.kv"))
        screen_manager.add_widget(Builder.load_file("./gui_main/configurator.kv"))

        return screen_manager

    def on_start(self):
        Clock.schedule_once(self.launch_app, 1)

    def launch_app(self, dt):
        screen_manager.current = "HomeScreen"


if __name__ == "__main__":
    PCConfigurator().run()
