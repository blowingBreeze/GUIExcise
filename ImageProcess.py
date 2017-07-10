# coding=UTF-8
from PIL import ImageGrab
from PIL import Image
import math
import operator
from functools import reduce
import Tool
from XMLPrase import *
import os
import sys


class ImageProcess:

	#用于初始化一些成员变量
	def __init__ (self):
		self.IMAGEPATH = Tool.Path.PERSONAL_DIR + "\\BnS\\TENCENT\\"
		self.F_Num = 0   #保存F键截图的数量
		self.LB_Num = 0
		self.RB_Num = 0
		self.K4_Num = 0
		self.V_Num = 0
		self.F_ImageList = []
		self.LB_ImageList = []
		self.RB_ImageLsit = []
		self.K4_ImageList = []
		self.V_ImageLisst = []
		self.SkillCoordi = UIPrase ()
		self.cutSideLen = self.SkillCoordi.gridWith / 2
		self.initNum ( 'LB' )
		self.initNum ( 'RB' )
		self.initNum ( 'F' )
		self.initNum ( '4' )
		self.initNum ( 'V' )



	def _getNum (self,prefix):
		if prefix == 'F' :
			return self.F_Num
		if prefix == 'LB':
			return self.LB_Num
		if prefix == 'RB':
			return self.RB_Num
		if prefix == '4':
			return self.K4_Num
		if prefix == 'V':
			return self.V_Num
	
	def _addNum (self,prefix,ad = 1):
		if prefix == 'F' :
			self.F_Num+=ad
		if prefix == 'LB':
			self.LB_Num+=ad
		if prefix == 'RB':
			self.RB_Num+=ad
		if prefix == '4':
			self.K4_Num+=ad
		if prefix == 'V':
			self.V_Num+=ad

	def _subNum (self,prefix,su = 1):
		if prefix == 'F' :
			self.F_Num-=ad
		if prefix == 'LB':
			self.LB_Num-=ad
		if prefix == 'RB':
			self.RB_Num-=ad
		if prefix == '4':
			self.K4_Num-=ad
		if prefix == 'V':
			self.V_Num-=ad

	def getBBox (self,prefix):
		if prefix == 'F' :
			return  ( self.SkillCoordi.coordi['F_X'] - 10,
				self.SkillCoordi.coordi['F_Y'] - 10,
				self.SkillCoordi.coordi['F_X'] +10,
				self.SkillCoordi.coordi['F_Y'] + 10)
		if prefix == 'LB':
			return  ( self.SkillCoordi.coordi['LB_X'] - 10,
				self.SkillCoordi.coordi['LB_Y'] -10,
				self.SkillCoordi.coordi['LB_X'] +10,
				self.SkillCoordi.coordi['LB_Y'] + 10 )
		if prefix == 'RB':
			return  ( self.SkillCoordi.coordi['RB_X'] -10,
				self.SkillCoordi.coordi['RB_Y'] - 10,
				self.SkillCoordi.coordi['RB_X'] +10,
				self.SkillCoordi.coordi['RB_Y'] +10 )
		if prefix == '4':
			return  ( self.SkillCoordi.coordi['K_4_X'] - 10,
				self.SkillCoordi.coordi['K_4_Y'] - 40,
				self.SkillCoordi.coordi['K_4_X'] + 10,
				self.SkillCoordi.coordi['K_4_Y'] -20 )
		if prefix == 'V':
			return  ( self.SkillCoordi.coordi['K_V_X'] - 10,
				self.SkillCoordi.coordi['K_V_Y'] - 40,
				self.SkillCoordi.coordi['K_V_X'] + 10,
				self.SkillCoordi.coordi['K_V_Y'] -20)

	def getList (self,prefix):
		if prefix == 'F' :
			return self.F_ImageList
		if prefix == 'LB':
			return self.LB_ImageList
		if prefix == 'RB':
			return self.RB_ImageLsit
		if prefix == '4':
			return self.K4_ImageList
		if prefix == 'V':
			return self.V_ImageLisst

	#保存某个按键的截图
	def saveImage (self,prefix):
		im = ImageGrab.grab ( bbox=self.getBBox ( prefix ) )
		im.save ( self.IMAGEPATH + prefix + '_' + str ( self._getNum ( prefix ) ) + '.png' )
		self._addNum ( prefix )
	
	def initNum (self,prefix):
		listFile = os.listdir ( self.IMAGEPATH )
		value = 0
		for image in listFile:
			if image[0:len ( prefix )] == prefix:
				value+=1
		if prefix == 'F' :
			self.F_Num = value
		if prefix == 'LB':
			self.LB_Num = value
		if prefix == 'RB':
			self.RB_Num = value
		if prefix == '4':
			self.K4_Num = value
		if prefix == 'V':
			self.V_Num = value


	#把截取的图像打开，以便于后面匹配图像
	def readyToCompare (self,prefix):
		listFile = os.listdir ( self.IMAGEPATH )
		for image in listFile:
			if image[0:len ( prefix )] == prefix:
				im = Image.open ( self.IMAGEPATH + image )
				self.getList ( prefix ).append ( im )

	#根据图片名称的前缀对比相应的图片，得到相同的图片时返回True
	def compareImage (self,prefix):
		compareList = self.getList ( prefix )
		realTimeImage = ImageGrab.grab ( self.getBBox ( prefix ) )

		h1 = realTimeImage.histogram ()

		for im in compareList:
			h2 = im.histogram ()
			result = math.sqrt ( reduce ( operator.add,  list ( map ( lambda a,b: ( a - b ) ** 2, h1, h2 ) ) ) / len ( h1 ) )
			if result > -0.000003 and result < 0.000003 :
				return True
	
