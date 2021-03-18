import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config

Config.set('graphics', 'resizable', 1)


class Calc(GridLayout):
    def vypocitej(self, pocty):
        if pocty:
            try:
                self.display.text = str(eval(pocty))
            except Exception:
                self.display.text = "Error"


class Kalkulacka(App):
    def build(self):
        return Calc()


calcApp = Kalkulacka()
calcApp.run()
