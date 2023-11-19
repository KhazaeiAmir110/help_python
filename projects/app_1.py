import kivy
from kivy.app import App
from kivy.uix import label, boxlayout, textinput, button
from kivy.core.window import Window

class MyApp(App):
    Window.size = (300, 500)

    def submit(self,click):
        if (self.text_name.text != "" and self.text_family.text != "" and self.text_country.text != ""):
            print(f"name : {self.text_name.text} \n family : {self.text_family.text} \n country : {self.text_country.text}")
            self.button.disabled = True
            self.button.text = "Thank you !!!"
            self.text_name.text = ""
            self.text_family.text = ""
            self.text_country.text = ""
            
        else:
            print("ERROR")

    def build(self):
        self.label_name = label.Label(text='please enter your name : ')
        self.text_name = textinput.TextInput(multiline=False)

        self.label_family = label.Label(text='please enter your family : ')
        self.text_family = textinput.TextInput(multiline=False)

        self.label_country = label.Label(text='please enter your country : ')
        self.text_country = textinput.TextInput(multiline=False)

        self.box = boxlayout.BoxLayout(orientation='vertical')
        self.button = button.Button(text='SEND',font_size=40, bold = True)

        # funstion
        self.button.bind(on_press=self.submit)


        self.box.add_widget(self.label_name)
        self.box.add_widget(self.text_name)

        self.box.add_widget(self.label_family)
        self.box.add_widget(self.text_family)

        self.box.add_widget(self.label_country)
        self.box.add_widget(self.text_country)

        self.box.add_widget(self.button)

        return self.box


if __name__ == "__main__":
    MyApp().run()