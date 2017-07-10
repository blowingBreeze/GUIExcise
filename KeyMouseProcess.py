from pymouse import PyMouse
from pykeyboard import PyKeyboard
from XMLPrase import *
import win32api

class KeyAndMouse:
	def __init__ (self):
		self.m = PyMouse ()
		self.k = PyKeyboard ()
		self.SkillCoordi = UIPrase ()
		self.ScreenWidth = win32api.GetSystemMetrics ( 0 )
		self.ScreenHeight = win32api.GetSystemMetrics ( 1 )

	def click_F (self):
		self.k.press_key ( 'f' )

	def click_LB (self):
		print self.m.position()
		self.m.click ( self.m.position()[0],
				self.m.position()[1],
			1 )

	def click_RB (self):
		self.m.click (self.m.position()[0],
				self.m.position()[1],
			2 )
		
	def click_4 (self):
		self.k.press_key ( '4' )

	def click_V (self):
		self.k.press_key ( 'v' )



