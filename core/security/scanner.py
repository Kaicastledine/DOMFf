#!/usr/env/python
# -*- coding: utf-8 -*-

import os,sys
from core.set.color import *
from core.security.warning import *

class security_scanner(object):
	def __init__(self):
		self.folder = ""
		self.index  = ""
		self.deprecated_warning = []

	def set_folder(self, folder):
		self.folder = folder

	def set_index(self, index):
		self.index = index

	def get_warning(self):
		return self.deprecated_warning

	def deprecated_file(self, folder):
		# print bcolors.OKBLUE + "[+] Check function update"+ bcolors.ENDC
		list_file = os.listdir(folder)
		for filename in list_file:
			if os.path.isdir(folder + "/" + filename):
				self.deprecated_file(folder + "/" + filename)
			else:
				if os.path.splitext(folder + "/" + filename)[1] == '.php':
					for line in function_php:
						open_file = open(folder + "/" + filename, 'r+')
						if line['function'] in open_file.read():
							add_format = {'file'   : folder + "/" + filename,
								          'warning': line['function'],
								          'replace': line['replace'],
								          'type'   : line['name']}
							self.deprecated_warning.append(add_format)
							if line['name'] == "rowCount":
								print self.deprecated_warning
								print line
								print folder + "/" +filename
								raw_input('>')
					open_file.close()

		# list_file = os.listdir(folder)
		# for filename in list_file:
		# 	if os.path.isdir(folder + "/" + filename):
		# 		self.deprecated_file(folder + "/" + filename)
		# 	else:
		# 		if os.path.splitext(folder + "/" + filename)[1] == '.php':
		# 			for line in function_php:
		# 				open_file = open(folder + "/" + filename, 'r+')
		# 				if line['deprecated'] in open_file.read():
		# 						add_format = {'file'   : folder + "/" + filename,
		# 						              'warning': line['deprecated'],
		# 						              'replace': line['replace'],
		# 						              'type'   : "function deprecated"}
		# 						self.deprecated_warning.append(add_format)
		# 			open_file.close()



