import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox

class MyApp(App):
    def build(self):
        ch_1 = CheckBox()
        lbl_1 = Label(text='blue')

        # default == True
        ch_2 = CheckBox(active=True)
        lbl_2 = Label(text='green')

        # choose == False , None
        ch_3 = CheckBox(disabled=True)
        lbl_3 = Label(text='yellow')

        ch_4 = CheckBox()
        lbl_4 = Label(text='black')

        ch_5 = CheckBox()
        lbl_5 = Label(text='white')

        box_1 = BoxLayout(orientation='horizontal')
        box_1.add_widget(lbl_1)
        box_1.add_widget(ch_1)

        box_2 = BoxLayout(orientation='horizontal')
        box_2.add_widget(lbl_2)
        box_2.add_widget(ch_2)

        box_3 = BoxLayout(orientation='horizontal')
        box_3.add_widget(lbl_3)
        box_3.add_widget(ch_3)

        box_4 = BoxLayout(orientation='horizontal')
        box_4.add_widget(lbl_4)
        box_4.add_widget(ch_4)

        box_5 = BoxLayout(orientation='horizontal')
        box_5.add_widget(lbl_5)
        box_5.add_widget(ch_5)

        super_box = BoxLayout(orientation='vertical')
        super_box.add_widget(box_1)
        super_box.add_widget(box_2)
        super_box.add_widget(box_3)
        super_box.add_widget(box_4)
        super_box.add_widget(box_5)

        return super_box

if __name__ == "__main__":
    MyApp().run()