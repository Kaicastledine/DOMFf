#!/usr/env/python
# -*- coding: utf-8 -*-

import sys,os
from core.set.color import *
from colorama import Fore, Back, Style
import uuid

class report(object):
	def __init__(self, title, folder_report, func_report, all_file):
		self.folder_report = folder_report
		self.func_report = func_report
		self.list_file = all_file
		self.app_title = title
		self.message_report = []

	def owasp_warning(self, warning):
		warning_array = {
						'FULL Path Disclosure':
							{
							"security":"medium",
							"message":"\nFull Path Disclosure (FPD) vulnerabilities enable the attacker to see the path to the webroot/file. e.g.: /home/omg/htdocs/file/. \nCertain vulnerabilities, such as using the load_file() (within a SQL Injection) query to view the page source, \nrequire the attacker to have the full path to the file they wish to view.\nOWASP: https://www.owasp.org/index.php/Full_Path_Disclosure\n"
							},
						'deprecated':
							{
							"security":"hight",
							"message":"\nDOMFf have found deprecated function in your application.\nThis can open vulnerabilities please use a replace statement\n"
						 	},
						 'rowCount':
						 	{
						 	"security":"information",
						 	"message":"\nDOMFf have found rowCount() in application.\nThis function is secure but warning with bad configuration.\nPlease add strlen() security with VARCHAR configuration and Admin access.\nBLACKHAT USA: https://www.blackhat.com/presentations/bh-usa-06/BH-US-06-Neerumalla.pdf\n"
						 	},
						 'include':
						 	{
						 	"security":"information",
						 	"message":"\nDOMFf have found include() with $_GET in applicatin.\nThis function is secure but dangerous with bad configuration.\nPlease verify $_GET var before include.\nPHP.NET: http://php.net/manual/en/function.include.php\nOWASP: https://www.owasp.org/index.php/Testing_for_Local_File_Inclusion\n"
						 	},
						 'RCE':
						 	{
						 	"security":"hight",
						 	"message":"\nDOMFf have found function"
						 	}
						}
		try:
			return warning_array[warning]
		except:
			return False
	
	def set_folder_report(self, report):
		self.folder_report = report

	def set_func_report(self, report):
		self.func_report = report

	def set_title(self, title):
		self.app_title = title

	def app_info(self):
		print "ok"
	def warning_show(self, nb_line = False):
		message_report = []
		if nb_line ==  False:
			nb_line = 0
		current = 0
		if len(self.func_report) > 0:
			for line in self.folder_report:
				# print bcolors.BOLD + "| APPNAME : "+self.app_title+bcolors.ENDC
				if line['type'] == "FULL Path Disclosure":
					if line['type'] not in message_report:
						print bcolors.WARNING + self.owasp_warning(line['type'])['message'] + bcolors.ENDC
						print bcolors.FAIL + bcolors.BOLD + "| (security) : " + self.owasp_warning(line['type'])['security'] + bcolors.ENDC
						message_report.append(line['type'])
						if line['type'] not in self.message_report:
								self.message_report.append(line['type'])
					print bcolors.FAIL + "| ("+line['file']+") Full Path Disclosure"+bcolors.ENDC
			try:
				for line in self.func_report:
					end_line = nb_line + 5
					current = current + 1
					if "deprecated" not in message_report:
						print bcolors.WARNING + self.owasp_warning('deprecated')['message'] + bcolors.ENDC
						print bcolors.FAIL + bcolors.BOLD + "| (security) : " + self.owasp_warning('deprecated')['security'] + bcolors.ENDC
						message_report.append('deprecated')
						if line['type'] not in self.message_report:
								self.message_report.append(line['type'])
					elif line['type'] == "rowCount":
						if line['type'] not in message_report:
							print bcolors.WARNING + self.owasp_warning(line['type'])['message'] + bcolors.ENDC
							print bcolors.FAIL + bcolors.BOLD + "| (security) : " + self.owasp_warning(line['type'])['security'] + bcolors.ENDC
							message_report.append(line['type'])
							if line['type'] not in self.message_report:
								self.message_report.append(line['type'])
					elif line['type'] == "include":
						if line['type'] not in message_report:
							print bcolors.WARNING + self.owasp_warning(line['type'])['message'] + bcolors.ENDC
							print bcolors.FAIL + bcolors.BOLD + "| (security) : " + self.owasp_warning(line['type'])['security'] + bcolors.ENDC
							message_report.append(line['type'])
							if line['type'] not in self.message_report:
								self.message_report.append(line['type'])
					if current == end_line:
						# raw_input(Back.GREEN + Fore.BLACK +' <enter> to follow detection and <^C> for exit' + Style.RESET_ALL)
						nb_line = end_line
						os.system('clear')
						self.warning_show(nb_line)
						break
					print bcolors.FAIL + "| ("+line['file']+")"+bcolors.ENDC
					print "| deprecated function : "+bcolors.FAIL+line['warning']+bcolors.ENDC
					if line['replace'] != "":
						print "| replace function : "+bcolors.OKGREEN+line['replace']+bcolors.ENDC
			except:
				print "ok ^"
		else:
			print bcolors.OKGREEN + "| No current warning" + bcolors.ENDC
		pass

	def set_file_list(self, report):
		self.list_file = report
		pass

	def export_remark(self):
		li_array = []
		for line in self.message_report:
			content = self.owasp_warning(line)
			line_content = "<li class='"+content['security']+"'>"+content['message'].replace('--------- ','')+"</li>"
			li_array.append(line_content)
		try:
			return " ".join(li_array)
		except:
			pass

	def export_warning(self):
		li_array = []
		for line in self.func_report:
			if line['type'] == "deprecated":
				replacement = ''
				if line['replace'] != '':
					replacement = '<li>replace function : <b>'+line['replace']+'</b></li>'
				line_content = '<li>('+line['file']+')</li><ul class="second-ul"><li class="alert">deprecated function : <b class="red">'+line['warning']+'</b></li>'+replacement+'</ul>'
			else:
				line_content = '<li>('+line['file']+')</li><ul class="second-ul"><li class="alert">warning function : <b class="red">'+line['warning']+'</b></li></ul>'
			li_array.append(line_content)
		try:
			return " ".join(li_array)
		except:
			pass

	def export(self):
		open_template = open('core/template/report.html', 'r+')
		name_report = str(uuid.uuid4())
		new_template = open('export/'+name_report+'.html', 'a+')
		with open('core/template/report.html') as f:
			for line in f:
				if "{{remark}}" in line:
					line = self.export_remark()
				if "{{content}}" in line:
					line = self.export_warning()
				new_template.write(line)
			new_template.close()
			f.close()
		return name_report
		pass

	def load_tools(self):
		os.system('clear')
		action = 0
		self.warning_show()
		export = self.export()
		raw_input(Back.GREEN + Fore.BLACK + "Report exported : " + os.getcwd() + "/export/" + export + ".html" + Style.RESET_ALL)
		while action == 0:
			user_input = raw_input('[DOMFf />] ')
			if user_input == "help":
				    print """____________________________________________________________
| appinfo          : (Load application information)
| warning          : (Load application Warning information)
| clear            : (Clear console)
| exit             : (Exit DOM Forensics Framework)
------------------------------------------------------------"""
			
			if user_input == "export":
				self.export()
			if user_input == "appinfo":
				self.app_info()
			if user_input == "clear":
				os.system('clear')
			if user_input == "warning":
				self.warning_show()
			if user_input == "exit":
				action = 1
