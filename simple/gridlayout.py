import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class AppGridLayout(App):
    def build(self):
        layout = GridLayout(cols = 3)
        layout_new = GridLayout(cols =2)

        layout_new.add_widget(Button(text='button new 1'))
        layout_new.add_widget(Button(text='button new 2'))
        layout_new.add_widget(Button(text='button new 3'))
        layout_new.add_widget(Button(text='button new 4'))

        layout.add_widget(Button(text='button1'))
        layout.add_widget(Button(text='button2'))
        layout.add_widget(Button(text='button3'))
        layout.add_widget(layout_new)
        layout.add_widget(Button(text='button5'))
        layout.add_widget(Button(text='button6'))
        layout.add_widget(Button(text='button7'))
        layout.add_widget(Button(text='button8'))
        layout.add_widget(Button(text='button9'))
        layout.add_widget(Button(text='button10'))
        layout.add_widget(Button(text='button11'))
        layout.add_widget(Button(text='button12'))
        layout.add_widget(Button(text='button13'))
        layout.add_widget(Button(text='button14'))
        layout.add_widget(Button(text='button15'))

        return layout




if __name__ == '__main__':
    AppGridLayout().run()