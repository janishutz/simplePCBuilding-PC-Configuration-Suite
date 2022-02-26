from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.popup import Popup


class MainScreen(Screen):
    pass


class AddComponent(Screen):
    pass


class ModifyComponent(Screen):
    pass


class RemoveComponent(Screen):
    pass


class RootScreen(ScreenManager):
    pass


kv = Builder.load_file("../gui/gui.kv")


class ComponentManager(App):
    def build(self):
        return kv


if __name__ == "__main__":
    ComponentManager().run()
