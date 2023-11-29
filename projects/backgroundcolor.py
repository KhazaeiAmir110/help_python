import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 
class MultipleSliderWidget(BoxLayout):
	pass

class Multiple_Slider(App):
	def build(self):
		return MultipleSliderWidget()

if __name__ == '__main__':
	Multiple_Slider().run()
