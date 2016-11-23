#!/usr/env/python
# -*- coding: utf-8 -*-

import os,sys
import time
from core.set.color import *
from core.fld.framework import *
from core import global_env

class gathering(object):
	def __init__(self):
		self.directory  = ""
		self.index_file = ""
		self.index_try = ['index.php','index.html','public/index.php','public/index.html','project/public/index.php','project/public/index.html','html/index.php','html/index.html']
		self.warning_return = []
		self.file_list = []
		self.app_title = ""

	def load_class(self):
		self.check_index()

	def hello(self):
		print self.directory

	def set_directory(self, directory):
		if directory.endswith("/"):
			directory = directory[:-1]
		self.directory = directory

	def set_title(self):
		if os.path.exists(self.directory + "/" + self.index_file):
			open_file = open(self.directory + "/" + self.index_file)
			if "<title>" in open_file.read():
				print open_file.read()
				if "</title>" in open_file.read():
					self.app_title = open_file.read().split('<title>')[1].split('</title>')[0]
					return True
		return False

	def get_title(self):
		if self.app_title != "":
			return self.app_title
		return False


	def set_all_file(self, folder = False):
		os.system('clear')
		print "[Loading file...]"
		time.sleep(0.5)
		if folder == False:
			file_list = os.listdir(self.directory)
			folder = self.directory
		else:
			file_list = os.listdir(folder)
		for file in file_list:
			if not os.path.isdir(folder + "/" + file):
				print folder+"/"+file+"\n"
				if folder + "/" + file not in self.file_list:
					self.file_list.append(folder + "/" + file)
			else:
				self.set_all_file(folder + "/" + file)


	def get_warning(self):
		return self.warning_return

	def get_all_file(self):
		return self.file_list

	def get_directory(self):
		return self.directory


	def set_index(self, index):
		self.index_file = index

	def check_index_folder(self):
		print bcolors.BOLD + "[+] scanning for Full Path Disclosure"+ bcolors.ENDC
		file_dir = os.listdir(self.directory)
		for line in file_dir:
			if os.path.isdir(self.directory + "/" + line):
				disclosure = 0
				for indexfile in self.index_try:
					if os.path.exists(self.directory + "/" + line + "/" + indexfile):
						disclosure = 1
						#print bcolors.OKGREEN + "  | Path disclosure not found <"+self.directory+"/"+line+"/>"+bcolors.ENDC
				if disclosure == 0:
					format_warning = {'file'   : self.directory+"/"+line,
					                  'warning': "Full Path Disclosure (FPD)",
					                  'replace': "",
					                  'type'   : "FULL Path Disclosure"}
					self.warning_return.append(format_warning)
		self.set_all_file()

	def check_index(self):
		print  "["+bcolors.BOLD +"~"+bcolors.ENDC+"] Load application information"
		if not os.path.isdir(self.directory):
			print bcolors.FAIL + "  | "+bcolors.ENDC+" can't find folder <"+self.directory+">"
		for file in self.index_try:
			if os.path.exists(self.directory+'/'+file):
				print bcolors.OKGREEN + "  | application index found <"+self.directory+"/"+file+"/>" + bcolors.ENDC
				self.index_file = file
				if self.set_title() == False:
					print bcolors.FAIL + "  | Can't get application title" + bcolors.ENDC
				self.check_index_folder()
				return True
		print bcolors.FAIL + "  | "+bcolors.ENDC+" can't find index file <"+self.directory+">"
		on = 0
		while on == 0:
			user_input = raw_input('[Please select index file />]: ')
			if user_input != "":
				if os.path.exists(self.directory + '/' + user_input):
					print bcolors.OKGREEN + "  | "+bcolors.ENDC+"application index found <"+self.directory+"/"+user_input+">"
					self.index_file = user_input
					on = 1
		return True
