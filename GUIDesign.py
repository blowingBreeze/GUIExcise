# coding=UTF-8
from Tkinter import *
from ImageProcess import *
from PIL import Image,ImageTk
from KeyMouseProcess import *
import threading
import pythoncom,pyHook


class GUIProcess:
	def __init__(self):
		self.imPro=ImageProcess()
		self.km=KeyAndMouse()
		self.boolStart=0
		self.root=Tk()
		self.root.title('剑灵取色卡刀')
		self.lable_Welcome=Label(self.root,text='这是剑灵的取色卡刀软件，使用详情请阅读 README.txt文件').grid(row=3,columnspan=7,padx=10,pady=10,ipadx=5,ipady=5)

		self.lable_LB=Label(self.root,text='LB').grid(row=5,column=0,padx=10,pady=10,ipadx=5,ipady=5)
		self.lable_RB=Label(self.root,text='RB').grid(row=6,column=0,padx=10,pady=10,ipadx=5,ipady=5)
		self.lable_F=Label(self.root,text='F').grid(row=7,column=0,padx=10,pady=10,ipadx=5,ipady=5)
		self.lable_4=Label(self.root,text='4').grid(row=8,column=0,padx=10,pady=10,ipadx=5,ipady=5)
		self.lable_V=Label(self.root,text='v').grid(row=9,column=0,padx=10,pady=10,ipadx=5,ipady=5)


		self.ButtonItem('捕捉图片',5,1,self.LB_cal)
		self.ButtonItem('捕捉图片',6,1,self.RB_cal)
		self.ButtonItem('捕捉图片',7,1,self.F_cal)
		self.ButtonItem('捕捉图片',8,1,self.K_4_cal)
		self.ButtonItem('捕捉图片',9,1,self.V_cal)
		self.ButtonItem('初始化',10,0,self.Init_cal,1,2)
		self.ButtonItem('开始',10,3,self.Start_cal,1,2)
		self.ButtonItem('暂停',10,6,self.Pause_cal,1,2)

	def ButtonItem(self,text,row,column,callback,rowspan=1,columnspan=1):
		bu=Button(self.root,text=text)
		bu.bind("<Button-1>",callback)
		bu.grid(row=row,column=column,padx=10,pady=10,ipadx=5,ipady=5,rowspan=rowspan,columnspan=columnspan)


	def LableCathItem(self,row,prefix=''):
		self.imPro.saveImage(prefix)
		imNum=self.imPro._getNum(prefix)
		im=Image.open(self.imPro.IMAGEPATH+prefix+'_'+str(imNum-1)+'.png')
		bm=ImageTk.PhotoImage(im)
		lb=Label(self.root,image=bm)
		lb.image=bm
		lb.grid(row=row,column=imNum+1,padx=10,pady=10,ipadx=5,ipady=5)
		

	def LB_cal(self,event):
		self.LableCathItem(5,'LB')
		

	def RB_cal(self,event):
		self.LableCathItem(6,'RB')

	def F_cal(self,event):
		self.LableCathItem(7,'F')

	def K_4_cal(self,event):
		self.LableCathItem(8,'4')

	def V_cal(self,event):
		self.LableCathItem(9,'V')

	def LabelInitItem(self,prefix,row):
		imNum=self.imPro._getNum(prefix)
		if imNum==0:
			return 
		for n in range(0,imNum):
			im=Image.open(self.imPro.IMAGEPATH+prefix+'_'+str(n)+'.png')
			bm=ImageTk.PhotoImage(im)
			lb=Label(self.root,image=bm)
			lb.image=bm 
			lb.grid(row=row,column=n+2,padx=10,pady=10,ipadx=5,ipady=5)

	def Init_cal(self,event):
		self.LabelInitItem('LB',5)
		self.LabelInitItem('RB',6)
		self.LabelInitItem('F',7)
		self.LabelInitItem('4',8)
		self.LabelInitItem('V',9)


	def simul_click(self):
		while(True):
			if self.boolStart==1:
				continue
			if self.imPro.compareImage('LB')==True:
				pass
				#self.km.click_LB()
			if self.imPro.compareImage('RB')==True:
				pass
				#self.km.click_RB()
			if self.imPro.compareImage('F')==True:
				self.km.click_F()
			if self.imPro.compareImage('4')==True:
				self.km.click_4()
			if self.imPro.compareImage('V')==True:
				self.km.click_V()

	def Start_cal(self,event):
		
		self.imPro.readyToCompare("LB")
		self.imPro.readyToCompare("RB")
		self.imPro.readyToCompare("F")
		self.imPro.readyToCompare("4")
		self.imPro.readyToCompare("V")
		
		t=threading.Thread(target=self.simul_click)
		t.setDaemon(True)
		t.start()


	def Pause_cal(self,event):
		self.boolStart=1-self.boolStart



		




		









