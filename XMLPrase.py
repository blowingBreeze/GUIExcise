# coding=UTF-8
from Tool import *
import xml.etree.ElementTree as ET
from win32api import GetSystemMetrics

class UIPrase:
	a=0
	def __init__(self):
		xm=open(Path.PERSONAL_DIR+"\\BnS\\TENCENT\\ClientConfiguration.xml",'r')
		xTree=ET.parse(xm)
		self.root=xTree.getroot()

		self.ScreenWidth=GetSystemMetrics(0)
		self.ScreenHeight=GetSystemMetrics(1)
		self.coordi={}

		for element in self.root:
			if element.attrib['name']=='hc-1-x':
				self.coordi['LB_X']=float(element.attrib['value'])*self.ScreenWidth
				continue
			if element.attrib['name']=='hc-1-y':
				self.coordi['LB_Y']=float(element.attrib['value'])*self.ScreenHeight
				continue
			if element.attrib['name']=='hc-2-x':
				self.coordi['RB_X']=float(element.attrib['value'])*self.ScreenWidth
				continue
			if element.attrib['name']=='hc-2-y':
				self.coordi['RB_Y']=float(element.attrib['value'])*self.ScreenHeight
				continue
			if element.attrib['name']=='hc-3-x':
				self.coordi['F_X']=float(element.attrib['value'])*self.ScreenWidth
				continue
			if element.attrib['name']=='hc-3-y':
				self.coordi['F_Y']=float(element.attrib['value'])*self.ScreenHeight
				continue
			if element.attrib['name']=='hc-5-x':
				self.coordi['K_1234_X']=float(element.attrib['value'])*self.ScreenWidth
				continue
			if element.attrib['name']=='hc-5-y':
				self.coordi['K_1234_Y']=float(element.attrib['value'])*self.ScreenHeight
				continue
			if element.attrib['name']=='hc-23-x':
				self.coordi['K_ZXCV_X']=float(element.attrib['value'])*self.ScreenWidth
				continue
			if element.attrib['name']=='hc-23-y':
				self.coordi['K_ZXCV_Y']=float(element.attrib['value'])*self.ScreenHeight
				continue

		self.gridWith=self.coordi['RB_X']-self.coordi['LB_X']

		self.coordi['K_4_X']=self.coordi['K_1234_X']+60
		self.coordi['K_4_Y']=self.coordi['K_1234_Y']

		self.coordi['K_V_X']=self.coordi['K_ZXCV_X']+60
		self.coordi['K_V_Y']=self.coordi['K_ZXCV_Y']