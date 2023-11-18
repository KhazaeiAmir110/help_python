import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout


class Input(App):
    def build(self):
        label_1 = Label(text='please enter your name:')
        text_1 = TextInput(multiline=False)
        # vertical == عمودی
        # horizontal == افقی
        box_1 = BoxLayout(orientation='vertical')
        
        box_1.add_widget(label_1)
        box_1.add_widget(text_1)

        return box_1

if __name__ == '__main__':
    Input().run()