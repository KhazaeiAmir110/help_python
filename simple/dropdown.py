import kivy
from kivy.app import App
from kivy.uix.label  import Label
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown

class Dropdown(App):
    def build(self):
        dropdown_new = DropDown()
        for item in range(6):
            btn = Button(text=f'button {item}', size_hint_y=None, height=30)
            dropdown_new.add_widget(btn)
        superbtn = Button(text='Dropdown', size_hint=(.3, .1), pos_hint={'x': .35, 'y': .45})
        superbtn.bind(on_release=dropdown_new.open)
        return superbtn


if __name__ == '__main__':
    Dropdown().run()