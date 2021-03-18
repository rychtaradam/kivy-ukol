from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MainApp(App):

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            self.solution.text = ""
        else:
            if current and (self.posledni_operace and button_text in self.operace):
                return
            elif current == "" and button_text in self.operace:
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.posledni_operace = self.last_button in self.operace

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution

    def build(self):
        self.operace = ["/", "*", "+", "-"]
        self.posledni_operace = None
        self.posledni_tlacitko = None
        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(multiline=False, readonly=True, halign="right", font_size=55)
        main_layout.add_widget(self.solution)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, pos_hint={"center_x": 0.5, "center_y": 0.5})
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        rovnase_btn = Button(text="=", pos_hint={"center_x": 0.5, "center_y": 0.5})
        rovnase_btn.bind(on_press=self.on_solution)
        main_layout.add_widget(rovnase_btn)

        return main_layout


if __name__ == "__main__":
    app = MainApp()
    app.run()
