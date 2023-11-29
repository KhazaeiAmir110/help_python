import kivy 
from kivy.app import App 
from kivy.uix.vkeyboard import VKeyboard 


class Test(VKeyboard): 
	player = VKeyboard() 


class VkeyboardApp(App): 
	def build(self): 
		return Test() 


if __name__ == '__main__': 
	VkeyboardApp().run() 
