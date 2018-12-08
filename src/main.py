from kivy.app import App
from kivy.uix.screenmanager import ScreenManager


class ForgScreenManager(ScreenManager):
    pass


class ForgApp(App):
    def build(self):
        return ForgScreenManager()


def main():
    ForgApp().run()


if __name__ == "__main__":
    main()
