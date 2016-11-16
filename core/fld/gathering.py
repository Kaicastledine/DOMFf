#!/usr/env/python
# -*- coding: utf-8 -*-

import os,sys
from core.set.color import *
from core.fld.framework import *

class gathering(object):
	def __init__(self):
		self.directory  = ""
		self.index_file = ""
		self.index_try = ['index.php','index.html','public/index.php','public/index.html','project/public/index.php','project/public/index.html','html/index.php','html/index.html']

	def set_directory(self, directory):
		if directory.endswith("/"):
			directory = directory[:-1]
		self.directory = directory

	def set_index(self, index):
		self.index_file = index

	def check_index(self):
		if not os.path.isdir(self.directory):
			print bcolors.FAIL + "| "+bcolors.ENDC+" can't find folder <"+self.directory+">"
			sys.exit()
		for file in self.index_try:
			if os.path.exists(self.directory+'/'+file):
				print bcolors.OKGREEN + "| "+bcolors.ENDC+" application index found <"+self.directory+"/"+file+">"
				self.index_file = file
				return True
		print bcolors.FAIL + "| "+bcolors.ENDC+" can't find index file <"+self.directory+">"
		on = 0
		while on == 0:
			user_input = raw_input('[Please select index file />]: ')
			if user_input != "":
				if os.path.exists(self.directory + '/' + user_input):
					print bcolors.OKGREEN + "| "+bcolors.ENDC+" application index found <"+self.directory+"/"+user_input+">"
					self.index_file = user_input
					on = 1
		return True
