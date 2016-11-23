#!/usr/env/python
# -*- coding: utf-8 -*-

import os,sys
import string
import random
import importlib
from core.set.color import *
from core.set.body import *
from core.fld.gathering import *
from core.security.scanner import *
from core.report.tools import *

base_url = ""

class AutoLoad():
	def __init__(self, argv):
		self.argv = argv

	def domff(self):
	    for argv in self.argv:
	        if len(self.argv) < 2:
	            print bcolors.FAIL + "| " + bcolors.ENDC + "Please use : python " + self.argv[0] + " --url=http://exemple.com"
	        elif "--url=" in self.argv[1]:
	            url_information = self.argv[1].split('--url=')
	            if "://" in url_information[1] or "www." in url_information[1]:
	                if "." in url_information[1]:
	                    if "www." in url_information[1] and not "://" in url_information[1]:
	                        url_information[1] = "http://" + url_information[1]
	                    base_url = url_information[1]
	                    header(base_url)
	        elif "--dir=" in argv:
	            folder = gathering()
	            folder.set_directory(argv.split("--dir=")[1])
	            folder.load_class()
	            scanner = security_scanner()
	            scanner.deprecated_file(folder.get_directory())
	            report_load = report(folder.get_title(), folder.get_warning(), scanner.get_warning(), folder.get_all_file())
	            report_load.load_tools()

	        elif "--dir=" not in self.argv[1] and "--url=" not in self.argv[1]:
	            print bcolors.FAIL + "| "+bcolors.ENDC + "Please use : python "+self.argv[0]+" --url=http://exemple.com"