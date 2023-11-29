import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup


class MyApp(App):
    def openp(self, btn):
        lable_1 = Label(text='This is inside of popup')
        btnClosePopup = Button(text='close popup')
        box = BoxLayout(orientation='vertical')
        box.add_widget(lable_1)
        box.add_widget(btnClosePopup)

        popup = Popup(title='Test of popup !!!', content=box)
        popup.open()

        btnClosePopup.bind(on_press=popup.dismiss)


    def build(self):
        btnOpenPopup = Button(text='Open it!')
        btnOpenPopup.bind(on_press=self.openp)
        return btnOpenPopup



if __name__ == '__main__':
    MyApp().run()