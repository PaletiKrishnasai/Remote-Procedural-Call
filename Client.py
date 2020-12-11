import tkinter
import os
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter import simpledialog  
from tkinter import ttk
import threading
import sys
import faulthandler
import socket
sys.setrecursionlimit(10**6)

def calculate(command):
	#host = '34.90.102.225'
	host = '127.0.0.1'
	port = 8080
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
	s.connect((host,port))
	while True: 
  
        # command sent to server
			
		s.send(bytes(command, 'utf-8'))
	  
		# recieved response
		data = s.recv(1024) 
	  
		# print the received response
		pi = float(str(data.decode('ascii')))
		#print("Pi recieved as:",pi) 

		r = 6
		area = pi*r*r
		circum = 2*pi*r
		command_output = "The Fixed radius is : "+str(r)+"\nThe Value of PI : "+str(pi)+"\nThe Area Calculated is: "+str(area)+"\nThe Circumference Calculated is: "+str(circum)+"\n"
		return command_output


class RPC:
	
	__root = Tk()
	
	__thisWidth = 300
	__thisHeight = 300
	
	__thisTextArea = Text(__root,bg="white",font="Arial",fg="black",highlightbackground="red",highlightcolor="green",insertbackground="black",selectbackground="cyan",wrap=WORD)
	__thisMenuBar = Menu(__root)
	__thisActionMenu = Menu(__thisMenuBar, tearoff = 0)
	__thisHelpMenu = Menu(__thisMenuBar, tearoff = 0)

	counter = 0
	
	def __init__(self,**kwargs):
		try:
			self.__root.wm_iconbitmap("Notepad.ico")
		except:
			pass
		
		try:
			self.__thisWidth = kwargs['width']
		except KeyError:
			pass
			
		try:
			self.__thisHeight = kwargs['height']
		except KeyError:
			pass
			
		self.__root.title("RPC")
		
		bindtags = list(self.__thisTextArea.bindtags())
		bindtags.remove("Text")
		self.__thisTextArea.bindtags(tuple(bindtags))
		
		"""If the height is not specified in the keyword arguments given, then use default values specified"""
		
		screenWidth = self.__root.winfo_screenwidth() 
		screenHeight = self.__root.winfo_screenheight() 
	
		left = (screenWidth / 2) - (self.__thisWidth / 2) 
		
		top = (screenHeight / 2) - (self.__thisHeight /2) 
		
		self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth,self.__thisHeight,left,top))
		
		self.__root.grid_rowconfigure(0,weight = 1)
		self.__root.grid_columnconfigure(0,weight = 1)
		
		self.__thisTextArea.grid(sticky = N + E + S + W) 
		
		
		self.__thisActionMenu.add_command(label = "Switch Theme",command = self.__theme)
		
		self.__thisActionMenu.add_command(label = "Enter Command",command = self.__command)
		
		self.__thisActionMenu.add_separator()
		self.__thisActionMenu.add_command(label = "Exit",command = self.__quitApplication, accelerator = "Ctrl + Q")
		
		self.__thisMenuBar.add_cascade(label = "Action",menu = self.__thisActionMenu)
		
		self.__thisHelpMenu.add_command(label = "About",command = self.__showAbout)

		self.__thisHelpMenu.add_command(label = "Group Members",command = self.__showGroup)
		
		self.__thisMenuBar.add_cascade(label = "Help",menu = self.__thisHelpMenu)
		
		self.__root.config(menu = self.__thisMenuBar)
			
	
	def __showAbout(self):
		showinfo("RPC","Made by Group 1")
		
	def __showGroup(self):
		showinfo("Group Members","COE18B024 - Hrishikesh Rajesh Menon \nCOE18B028 - Katepalli Naga Sai Bhargav\nCOE18B056 - Thigulla Vamsi Krishna\nCOE18B065 - Srinivasan R Sharma\nCED18I039 - Paleti Krishnasai\nCED18I056 - Vasupalli Surya Satya Darshan")
		
	def __theme(self):
		if self.counter!=0:
			self.__thisTextArea.config(bg="white",font="Arial",fg="black",highlightbackground="red",highlightcolor="green",insertbackground="black",selectbackground="cyan",wrap=WORD)
			self.counter = 0
		else:
			self.__thisTextArea.config(bg="black",font="Arial",fg="white",highlightbackground="red",highlightcolor="green",insertbackground="white",selectbackground="yellow",wrap=WORD)
			self.counter = 1
			
	
	def __quitApplication(self,event = None):
		if messagebox.askokcancel("Quit","Do you wish to exit the application?"):
			self.__root.destroy()
			
	def run(self):
		self.__root.mainloop()
		
	def __command(self):
		command = simpledialog.askstring("Command","Enter the number of points to take ")
		command_output = "Output"
		print(command)
		if command !="":
			if (int(command) > 0):
				command_output = calculate(command)	
				self.__thisTextArea.delete(1.0,END)
				#command_output = "The Area is: "+str(area)+"\nThe Circumference is: "+str(circum)+"\n"
				self.__thisTextArea.insert(1.0,command_output)
	
				op_continue = messagebox.askyesno("Continue Operations","Do you want to continue operations?")
			else:
				op_continue = messagebox.askyesno(
				"Continue Operations", "INVALID INPUT\nDo you want to continue operations?")
		else:
			op_continue = messagebox.askyesno(
				"Continue Operations", "INVALID INPUT\nDo you want to continue operations?")

		if op_continue:
			self.__command()
		else:
			self.__quitApplication()
		
		
RP = RPC(width=600,height=400)
RP.run()
		
