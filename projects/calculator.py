import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout 


class MyGridLayout(GridLayout):
	def calc(self,event):
		if event : #3/0
			try:
				self.display.text = str(eval(event))
			except:
				self.disabled.text = 'ERROR'

class CalculatorApp(App):
	def build(self):
		return MyGridLayout()

if __name__ == '__main__':
	CalculatorApp().run()
