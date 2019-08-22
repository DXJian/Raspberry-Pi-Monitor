# -*- coding: UTF-8 -*-
import sys
import RPi.GPIO as GPIO
import time
import sys
from steering import Steering
import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.options
from tornado.options import define,options
import configparser
import RPi.GPIO as GPIO

from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from tornado.options import define, options, parse_command_line
from tornado.httpserver import HTTPServer
import os.path



define("port",default=80,type=int)

class Camera:
	def __init__(self):

		config = configparser.ConfigParser()
		config.read("./config.ini")
		HIntfNum = config.getint("camera", "HIntfNum")
		HInitPosition = config.getint("camera", "HInitPosition")
		HMinPosition = config.getint("camera", "HMinPosition")
		HMaxPosition = config.getint("camera", "HMaxPosition")
		HSpeed = config.getint("camera", "HSpeed")

		# Vertical direction control parameters
		VIntfNum = config.getint("camera", "VIntfNum")
		VInitPosition = config.getint("camera", "VInitPosition")
		VMinPosition = config.getint("camera", "VMinPosition")
		VMaxPosition = config.getint("camera", "VMaxPosition")
		VSpeed = config.getint("camera", "VSpeed")
 
		self.HCameraControl = Steering(HIntfNum, HInitPosition,
		 HMinPosition, HMaxPosition, HSpeed)
		
		self.VCameraControl = Steering(VIntfNum, VInitPosition,
		 VMinPosition, VMaxPosition, VSpeed)
    
	def cameraRotate(self,direction):

		if direction == "A":
			self.HCameraControl.forwardRotation()

		elif direction == "D":
			self.HCameraControl.reverseRotation()

		elif direction == "W":
			self.VCameraControl.forwardRotation()

		elif direction == "S":
			self.VCameraControl.reverseRotation()

		elif direction == "R":
			self.HCameraControl.reset()
			self.VCameraControl.reset()

		else:
			print("Your input for camera direction is wrong, please input: D, A, W, S or RESET!")

camera = Camera()
def run(dir):	
	camera.cameraRotate(dir)



class IndexHandler(tornado.web.RequestHandler):
		            
		def get(self):
                
			self.render("index.html",encoding="utf8")
        
		def post(self):             
 
# Horiazonal direction control parameters
			arg = self.get_argument('k')

			if(arg=='w'):
				dir = "W"
				run(dir)
			    
			elif(arg=='s'):
				dir = "S"
				run(dir)

			elif(arg=='a'):
				dir = "A"
				run(dir)

			elif(arg=='d'):
				dir = "D"
				run(dir)

			#elif(arg=='r'):
             #   self.HCameraControl.reset()
              #  self.VCameraControl.reset()
			else:
				return False
			self.write(arg)

if __name__ == '__main__':       
		tornado.options.parse_command_line()
		app = tornado.web.Application(handlers=[(r"/",IndexHandler)],static_path=os.path.join(os.path.dirname(__file__), "static"),)
		http_server = tornado.httpserver.HTTPServer(app)
		http_server.listen(options.port)
		tornado.ioloop.IOLoop.instance().start()