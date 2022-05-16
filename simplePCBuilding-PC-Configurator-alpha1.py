# This is the main runtime of the simplePCBuilding-PC-Configurator
# IMPORTS
import datetime
import configparser
import logging
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.clock import mainthread
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock

config = configparser.ConfigParser()
config.read('./config/settings.ini')

version_app = f"{config['Info']['version']}{config['Info']['subVersion']}"

################################################################
# LOGGER SETUP
##################
logging.basicConfig(level=logging.DEBUG, filename="./log/main_log.log", filemode="w")
logs = f"./log/{datetime.datetime.now()}-log-main.log"
logger = logging.getLogger(__name__)
handler = logging.FileHandler(logs)
formatter = logging.Formatter("%(levelname)s - %(asctime)s - %(name)s: %(message)s -- %(lineno)d")
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.setLevel(config['Dev Settings']['log_level'])
logger.info(f"Logger initialized, app is running Version: {version_app}")
################################################################



###########
# SCREENS
###########


class Splash(MDScreen):
    pass


class Home(MDScreen):
    pass


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
        self.icon = "./data/Logo.png"
        screen_manager.add_widget(Builder.load_file("./gui_main/splashscreen.kv"))
        screen_manager.add_widget(Builder.load_file("./gui_main/main-gui.kv"))
        screen_manager.add_widget(Builder.load_file("./gui_main/configurator.kv"))
        screen_manager.add_widget(Builder.load_file("./gui_main/settings.kv"))
        return screen_manager

    def on_start(self):
        logger.info("App mainframe started, executing checks")
        Clock.schedule_once(self.launch_app, 1)

    def launch_app(self, dt):
        # Here the launch script will be launched and the screen will automatically be changed to the home screen
        screen_manager.current = "HomeScreen"


if __name__ == "__main__":
    logger.info("Launching App...")
    PCConfigurator().run()
