import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class Input(App):
    def build(self):
        label_1 = Label(text='please enter your name:', font_size=40,color='red')
        text_1 = TextInput(multiline=False)
        self.text_1 = text_1
        button_1 = Button(text='send', font_size=40, bold=True, background_color='blue', size_hint=(0.5,0.2))
        button_1.bind(on_press=self.press_key)


        box_1 = BoxLayout(orientation='vertical')
        
        box_1.add_widget(label_1)
        box_1.add_widget(text_1)
        box_1.add_widget(button_1)

        return box_1


    def press_key(self,event):
        self.text_1.text = "your name is sending!!!!!!!!!"
if __name__ == '__main__':
    Input().run()