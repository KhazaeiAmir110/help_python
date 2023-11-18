import kivy
from kivy.app import App
from kivy.uix.button import Button


class Input(App):
    def build(self):
        return Button(size_hint=(.2,.2), pos_hint={'x':.4 , 'y':.4}, background_normal='./images/images (1).jpg', background_down='./images/images.jpg')
if __name__ == '__main__':
    Input().run()