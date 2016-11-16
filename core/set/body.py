#!/usr/env/python
# -*- coding: utf-8 -*-

import time
import os,sys
import urllib2
from core.set.settings import theme,list_agent
from colorama import Fore, Back, Style
from bs4 import BeautifulSoup
from datetime import datetime
import uuid
from core.set.color import *
source_code = ""
header_information = ""
extract_line = ""
web_url = ""
page_url = ""
move_stuct = {'move':'','return':''}
jump_list = []
lecture = 0
breaked_list = []
mark = []
search_list = []
new_url = ""
resume_jump = ""
log_online = "off"
log_file = ""
link_listing = []
link_global = []
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36"
global_cookie = ""
class listen_logs(object):
    global link_listing
    global log_online
    global log_file
    def __init__(self):
        self.online = log_online
        self.file = log_file
        self.path = os.getcwd()+"/logs/"
    def start(self):
        self.generate_file()
        self.make_element()
    def stop(self):
        print bcolors.WARNING + "| Listen logs stop"+bcolors.ENDC
    def generate_file(self):
        global log_file
        if self.file == "":
            self.file = str(uuid.uuid4())+".domff"
            log_file = self.file
    def make_element(self):
        if os.path.isfile(self.path+self.file):
            print bcolors.OKGREEN + "| resume logs : " +self.path+self.file+bcolors.ENDC
        elif not os.path.isfile(self.path+self.file):
            if not os.path.exists(self.path):
                os.makedirs(self.path)
            file_logs = open(self.path+self.file,'a+')
            file_logs.write('[+] start listen : '+str(datetime.now())+"\n")
            file_logs.close()
            print bcolors.OKGREEN + "| Listen logs start : "+self.path+self.file+bcolors.ENDC
            return self.file
        else:
            print bcolors.FAIL + "| Error on listening logs."+bcolors.ENDC
    def make_header(self,header):
        global log_file
        global web_url
        if self.online == "on":
            print "enter"
            file_logs = open(self.path+log_file,'a+')
            file_logs.write("-----------------------\n")
            file_logs.write("header : "+web_url+"\n")
            file_logs.write("-----------------------\n")
            split_header = str(header).split("\n")
            for line in split_header:
                if line != "":
                    file_logs.write("| "+line+"\n")
            file_logs.close()
    def make_map_link(self):
        global link_listing
        if self.online == "on":
            file_logs = open(self.path+self.file,'a+')
            file_logs.write("-----------------------\n")
            file_logs.write("Map link\n")
            file_logs.write("-----------------------\n")
            for element in link_listing:
                file_logs.write("| " + element['website']+"\n")
                for link in element['link']:
                    file_logs.write("  | "+ link+"\n")



class analysing(object):
    def __init__(self):
        self.sourcecode = ""
        self.type = ""
        self.name = ""
        self.id = ""
        self.value = ""
        self.method = ""
        self.action = ""
        self.param = {}
        self.param_id = 0
        self.url = ""
        self.pages = ""
        self.jump_list = []

    def reset(self):
        self.action = ""
        self.value = ""
        self.method = ""
        self.param = {}
        self.param_id = 0
        self.type = ""

    def menuForm(self, input_list):
        print """____________________________________________________________
| show             : Show params loaded data.
| sqlmap           : Generate SQLMAP line with current params.
| vuln             : Show possible vulnerability.
| help             : Show this help bullet.
| <enter>          : Skip this data.
------------------------------------------------------------"""
        action = 0
        while action == 0:
            user_input = raw_input("DOMFf:"+bcolors.WARNING+"FORM"+bcolors.ENDC+" > ")
            if user_input == "skip" or user_input == "":
                action = 1
            if user_input == "show":
                self.showparam(input_list)
            if user_input == "sqlmap":
                self.sqlmap(input_list)
            if user_input == "help":
                self.menuForm(input_list)
    def showparam(self, input_list):
        for input in input_list:
            value = input.get('value')
            name = input.get('name')
            type = input.get('type')
            if name != None and value != None:
                try:
                    print bcolors.BOLD + "-" + bcolors.ENDC + " (" + str(type) + ") " + str(name) + "=" + str(value)
                except:
                    print bcolors.FAIL + "| "+bcolors.ENDC+"Can't get this param (NO UTF)"
    def sqlmap(self, input_list):
        if self.method.lower() == "post":
            chains = ""
            for input in input_list:
                value = input.get('value')
                name = input.get('name')
                if name != None and value != None:
                    chains += "&" + name + "=" + value
            base = "| python sqlmap.py -u '" + self.action + "' --data='"+chains+"'"
            print base
        if self.method.lower() == "get":
            chains = ""
            for input in input_list:
                value = input.get('value')
                name = input.get('name')
                if name != None and value != None:
                    if chains == "":
                        chains += "?" + name + "=" + value
                    else:
                        chains += "&" + name + "=" + value
            if "://" in self.action:
                base = "| python sqlmap.py -u '" + self.action + chains +"'"
            else:
                base = "| python sqlmap.py -u '" + self.url + self.action + chains + "'"
            print base

def std_report():
    global source_code
    print source_code


def extract_value(line):
    print Back.WHITE + Fore.BLACK+"--- EXTRACT VALUE ---"+ Style.RESET_ALL
    try:
        print "  |action: " + line.split('action="')[1].split('"')[0]
    except:
        try:
            print "  |action: " + line.split("action='")[1].split("'")[0]
        except:
            print "  |action: NO_ACTION"
    try:
        print "  |method: " + Fore.GREEN+line.split('method="')[1].split('"')[0]+Style.RESET_ALL
    except:
        try:
            print "  |method: " + Fore.GREEN + line.split("method='")[1].split("'")[0] + Style.RESET_ALL
        except:
            print "  |method: NO_METHOD"
    try:
        print "  |input : " + Fore.GREEN+line.split('type="')[1].split('"')[0]+Style.RESET_ALL
    except:
        try:
            print "  |input : " + Fore.GREEN + line.split("type='")[1].split("'")[0] + Style.RESET_ALL
        except:
            print "  |input : NO_INPUT_TYPE"
    try:
        print "  |value : " + Fore.GREEN+line.split('value="')[1].split('"')[0]+Style.RESET_ALL
    except:
        try:
            print "  |value : " + Fore.GREEN + line.split("value='")[1].split("'")[0] + Style.RESET_ALL
        except:
            print "  |value : NO_VALUE"
    try:
        print "  |name  : " + Fore.GREEN+line.split('name="')[1].split('"')[0]+Style.RESET_ALL
    except:
        try:
            print "  |name  : " + Fore.GREEN + line.split("name='")[1].split("'")[0] + Style.RESET_ALL
        except:
            print "  |name  : NO_NAME"
    try:
        print "  |class : " + Fore.GREEN+line.split('class="')[1].split('"')[0]+Style.RESET_ALL
    except:
        try:
            print "  |class : " + Fore.GREEN + line.split("class='")[1].split("'")[0] + Style.RESET_ALL
        except:
            print "  |class : NO_CLASS"
    try:
        print "  |id    : " + Fore.GREEN+line.split('id="')[1].split('"')[0]+Style.RESET_ALL
    except:
        try:
            print "  |id    : " + Fore.GREEN + line.split("id='")[1].split("'")[0] + Style.RESET_ALL
        except:
            print "  |id    : NO_ID"
    try:
        print "  |href   : "+Fore.GREEN+line.split('href="')[1].split('"')[0] + Style.RESET_ALL
    except:
        try:
            print "  |href  : " + Fore.GREEN + line.split("href='")[1].split("'")[0] + Style.RESET_ALL
        except:
            print "  |href  : NO_LINK"

    print Back.WHITE + Fore.BLACK+"--- EXTRACT VALUE ---" + Style.RESET_ALL

def extract(line):
    extract_value(line)


def forensics_menu():
    print """____________________________________________________________
| header           : (Show information of header)
| useragent        : (Change current user-agent)
| cookie           : (Update cookie)
| analyser         : (Start DOM forensics)
| get_form         : (Get all form)
| jmp:{element}    : (JUMP object on DOM exemple (jmp:FORM))
| jmp:list         : (Show JMP elements listing)
| jmpdel:{element} : (Delete element to JMP list)
| brk:{element}    : (Breakpoint on specific DOM element)
| brk:list         : (Show breakpoint listing)
| brkdel:{element} : (Delete element to breakpoint)
| set:{url}        : (Set new url)
| bk_url           : (Show back url)
| mov              : (Run forensics on new url)
| reboot           : (Reboot current request)
| import_link      : (Import all link)
| map_link         : (View map of links)
| network          : (View network map)
| clear_link       : (Clear link listing)
| clear            : (Clear current console)
| help - ls        : (Show this message help)
| log:on           : (Start logs)
| log:off          : (Stop logs)
| exit             : (Exit DOM Forensics Framework)
------------------------------------------------------------"""

def follow_link_mov(line):
    if "href=" in line:
        if "href='" in line:
            link = line.split("href='")[1].split("'")[0]
            if "//" in link[:2]:
                link = "http:" + link
            elif link[:1] == "/":
                link = web_url + link
            elif link[:1] == "#":
                link = web_url + "/" + link
            elif link[:3] != "htt":
                link = web_url + "/" + link
            print bcolors.OKGREEN + "| moving to : " + link + bcolors.ENDC
            header(link,move_cmd=True)
        elif 'href="' in line:
            link = line.split('href="')[1].split('"')[0]
            if "//" in link[:2]:
                link = "http:" + link
            elif link[:1] == "/":
                link = web_url + link
            elif link[:1] == "#":
                link = web_url + "/" + link
            elif link[:3] != "htt":
                link = web_url + "/" + link
            print bcolors.OKGREEN + "| moving to : "+link+bcolors.ENDC
            header(link.strip(), move_cmd=True)

def analyser():
    os.system('clear')
    global theme
    global mark
    global breaked_list
    global source_code
    global web_url
    global page_url
    global jump_list
    global resume_jump
    global lecture
    global extract_line
    global move_stuct
    analyse = analysing()
    analyse.url = web_url
    analyse.pages = page_url
    analyse.jump_list = jump_list
    analyse.sourcecode = source_code
    current_jmp = ",".join(jump_list)
    lecture = 0
    count_line = 0
    counter = 0
    breaked = 0
    old_line = 5
    while lecture == 0:
        if old_line >= len(source_code.split('\n')):
            print "end"
            lecture = 1
            break
        elif counter <= old_line:
            print Back.GREEN + Fore.BLACK + "| Open forensics on " + web_url + page_url + Style.RESET_ALL
            if resume_jump != "":
                old_line = int(resume_jump,16)
                resume_jump = ""
            for line in source_code.split('\n'):
                for theming in theme['BOLD']:
                    if theming in line:
                        line = line.replace(theming,bcolors.BOLD + theming + bcolors.ENDC)
                for theming in theme['GREEN']:
                    if theming in line:
                        line = line.replace(theming, bcolors.OKGREEN + theming + bcolors.ENDC)
                for theming in theme['YELLOW']:
                    if theming in line:
                        line = line.replace(theming, Fore.YELLOW + theming + bcolors.ENDC)
                if counter <= old_line:
                    for breaking_point in search_list:
                        if "<" + breaking_point in line:
                            if hex(count_line) not in breaked_list:
                                print Back.RED + "|BREAK|" + Fore.WHITE + line.strip() + Style.RESET_ALL
                                breaked_list.append(hex(count_line))
                                waiting = 0
                                while waiting == 0:
                                    user_input = raw_input(Fore.YELLOW+'breakpoint please enter <continue>: '+Style.RESET_ALL)
                                    if user_input == "continue":
                                        waiting = 1
                                breaked = 1
                    if move_stuct['move'] != '' and hex(count_line) == move_stuct['move']:
                        move_stuct['return'] = web_url + page_url
                        follow_link_mov(line)
                    if extract_line == hex(count_line):
                        print bcolors.OKBLUE + "|" + hex(count_line) + "|" + bcolors.ENDC + line.strip()
                        extract(line)
                    if hex(count_line) in mark and breaked == 0:
                        print bcolors.OKBLUE + "|" + hex(count_line) + "|" + bcolors.ENDC + Back.YELLOW + Fore.BLACK + line.strip() + Style.RESET_ALL
                    elif breaked == 0:
                        print bcolors.OKBLUE + "|" + hex(count_line) + "|" + bcolors.ENDC + line.strip()
                    breaked = 0
                else:
                    count_line = 0
                    user_input = raw_input('[DOMFf/>]: ')
                    if "jmp:" in user_input:
                        separate = user_input.split('jmp:')
                        if " " not in separate[1]:
                            if "0x" in separate[1]:
                                resume_jump = separate[1]
                                lecture = 1
                                print bcolors.OKGREEN+"|"+bcolors.ENDC+" Next analyser start on : "+separate[1]
                                break
                            else:
                                print bcolors.FAIL + "| jmp syntax not good please use jmp:0x"+bcolors.ENDC
                        else:
                            print bcolors.FAIL+"| jmp syntax not good please use jmp:0x"+bcolors.ENDC
                    elif "exit" in user_input:
                        lecture = 1
                        os.system('clear')
                        break
                    elif "mov:" in user_input:
                        separate = user_input.split('mov:')
                        if " " not in separate[1]:
                            if "0x" in separate[1]:
                                move_stuct['move'] = separate[1]
                                move_stuct['return'] = web_url+page_url
                                os.system('clear')
                                counter = 0
                                old_line+=1
                                break
                    elif user_input == "return":
                        if move_stuct['return'] != "":
                            os.system('clear')
                            move_stuct['move'] = ""
                            counter = 0
                            header(move_stuct['return'],move_cmd=True)
                    elif "extract:" in user_input:
                        separate = user_input.split('extract:')
                        if " " not in separate[1]:
                            if "0x" in separate[1]:
                                extract_line = separate[1]
                                os.system('clear')
                                counter = 0
                                old_line+= 1
                                break
                        extract(user_input)
                    elif "mark:" in user_input:
                        separate = user_input.split('mark:')
                        if " " not in separate[1]:
                            if "0x" in separate[1]:
                                if separate[1] not in mark:
                                    mark.append(separate[1])
                                else:
                                    mark.remove(separate[1])
                                os.system('clear')
                                counter = 0
                                old_line += 1
                                break
                            else:
                                print bcolors.FAIL + "| marker syntax not good please use mark:0x" + bcolors.ENDC
                        else:
                            print bcolors.FAIL + "| marker syntax not good please use mark:0x" + bcolors.ENDC
                    elif "set:" in user_input:
                        separate = user_input.split('set:')
                        if " " not in separate[1]:
                            if not "0x" in separate[1]:
                                line = int(separate[1],16)
                                old_line = old_line + line
                                print bcolors.OKGREEN + "| Position on : " + hex(old_line) + bcolors.ENDC
                            else:
                                print bcolors.FAIL + "| Set syntax not good please use set:<int>" + bcolors.ENDC
                        else:
                            print bcolors.FAIL + "| Set syntax not good please use set:0x" + bcolors.ENDC
                    elif user_input == "help":
                        print """____________________________________________________________
| jmp:<0x00>     : (resume later analyser to this address)
| extract:<0x00> : (Extract tag information)
| mark:<0x00>    : (Use marker on this address)
| mov:<0x00>     : (Move to link)
| return         : (return to last link)
| exit           : (Exit current session)
| set:<nb>       : (Jump +nb line)
____________________________________________________________"""
                    else:
                        os.system('clear')
                        counter = 0
                        old_line += 1
                        break
                counter += 1
                count_line +=1
        else:
            lecture = 1

def show_header():
    global header_information
    split_header = str(header_information).split("\n")
    for line in split_header:
        if line != "":
            print bcolors.OKGREEN + "| " +bcolors.ENDC+line
    logs = listen_logs()
    logs.make_header(header_information)


def debug(line):
    global jump_list
    global search_list
    global global_cookie
    global new_url
    global web_url
    if "jmp:" in line:
        separate = line.split('jmp:')
        if not " " in separate[1]:
            if separate[1] == "list":
                for line in jump_list:
                    print bcolors.BOLD+"|"+bcolors.ENDC+" <"+line+">"
            else:
                jump_list.append(separate[1])
                print bcolors.OKBLUE+"| (<"+separate[1]+">) element added to jump list"+bcolors.ENDC
        else:
            print bcolors.FAIL + "| Format is not available please exemple jmp:div,jmp:form..." + bcolors.ENDC
    elif "jmpdel:" in line:
        separate = line.split('jmpdel:')
        if not " " in separate[1]:
            if separate[1] in jump_list:
                jump_list.remove(separate[1])
                print bcolors.BOLD + "|"+bcolors.ENDC+" element <"+separate[1]+"> removed"
            else:
                print bcolors.FAIL + "| element not found in jump list"+ bcolors.ENDC
        else:
            print bcolors.FAIL + "| Format is not available please exemple jmpdel:div,jmpdel:form..." + bcolors.ENDC
    elif "brk:" in line:
        separate = line.split('brk:')
        if not " " in separate[1]:
            if separate[1] == "list":
                for line in search_list:
                    print bcolors.BOLD + "|" + bcolors.ENDC + " <" + line + ">"
            elif separate[1] not in search_list:
                search_list.append(separate[1])
                print bcolors.BOLD + "|" + bcolors.ENDC + " breaking on <" + separate[1] + ">"
            else:
                print bcolors.WARNING + "| element already found in breaking list" + bcolors.ENDC
        else:
            print bcolors.FAIL + "| Format is not available please exemple brk:div,brk:form..." + bcolors.ENDC
    elif "brkdel:" in line:
        separate = line.split('brkdel:')
        if not " " in separate[1]:
            if separate[1] in search_list:
                search_list.remove(separate[1])
                print bcolors.BOLD + "|" + bcolors.ENDC + " element <" + separate[1] + "> removed"
            else:
                print bcolors.FAIL + "| element not found in breakpoint list" + bcolors.ENDC
        else:
            print bcolors.FAIL + "| Format is not available please exemple brkdel:div,brkdel:form..." + bcolors.ENDC
    elif "set:" in line:
        separate = line.split('set:')
        if " " not in separate[1]:
            if "://" in separate[1] or "www." in separate[1]:
                if "." in separate[1]:
                    if "www." in separate[1] and not "://" in separate[1]:
                        separate[1] = "http://" + separate[1]
                    print bcolors.OKGREEN + "| "+bcolors.ENDC+"new url : "+separate[1]
                    new_url = separate[1]
    elif line == "mov":
        if new_url != "":
            loading = "/"
            x = 0
            while x < 5:
                os.system('clear')
                print "[" +bcolors.OKGREEN+ loading + bcolors.ENDC +"] Loading new url : " + new_url
                if loading == "/":
                    loading = '\\'
                elif loading == "\\":
                    loading = "/"
                time.sleep(0.1)
                x+=1
            os.system('clear')
            if global_cookie != "":
                input_u = raw_input(bcolors.BOLD + 'MOV new url with current cookie [y/N]? ')
                if input_u == "" or input_u == "n" or input_u == "N":
                    global_cookie = ""
            header(new_url)
        else:
            print bcolors.FAIL + "| Url empty please sur set:"+bcolors.ENDC


def import_link():
    global web_url
    global page_url
    global source_code
    global link_listing
    soup = BeautifulSoup(source_code, "html.parser")
    element = {'website': web_url + page_url, 'link': []}
    for link in soup.find_all('a', href=True):
        if "//" in link['href'][:2]:
            link['href'] = "http:"+link['href']
        elif link['href'][:1] == "/":
            link['href'] = web_url+link['href']
        elif link['href'][:1] == "#":
            link['href'] = web_url + "/"+link['href']
        elif link['href'][:3] != "htt":
            link['href'] = web_url+"/"+link['href']
        if link['href'] not in link_global:
            if link['href'] != "":
                print bcolors.OKGREEN+"|"+bcolors.ENDC+" New link imported : " + link['href']
                element['link'].append(link['href'])
                link_global.append(link['href'])
    link_listing.append(element)

def network():
    global link_listing
    space = ""
    key = 0
    for element in link_listing:
        if key == 0:
            print bcolors.BOLD + bcolors.OKBLUE + "|"+bcolors.ENDC+element['website']
        else:
            print bcolors.BOLD+space+"|"+bcolors.ENDC+element['website']
        key += 1
        space += " "

def map_link():
    logs = listen_logs()
    global link_listing
    for element in link_listing:
        print bcolors.BOLD+bcolors.OKBLUE + "| "+bcolors.ENDC+element['website']
        for link in element['link']:
            print bcolors.BOLD + "  | "+bcolors.ENDC+link
    logs.make_map_link()

def get_form():
    global source_code
    global web_url
    global page_url
    analyse = analysing()
    analyse.url = web_url
    analyse.pages = page_url
    analyse.jump_list = jump_list
    analyse.sourcecode = source_code
    soup = BeautifulSoup(source_code, "html.parser")
    form = soup.find_all('form')
    if not form:
        print "| No form on pages"
    else:
        for element in form:
            print bcolors.UNDERLINE + web_url + bcolors.ENDC
            print "|__" + bcolors.BOLD+page_url+bcolors.ENDC
            try:
                print bcolors.BOLD + "|_type :" + bcolors.ENDC + " FORM (" + element.get('name') + ")"
            except:
                print bcolors.BOLD + "|_type :" + bcolors.ENDC + " FORM (NO_NAME)"
            try:
                print bcolors.BOLD + "|_action:" + bcolors.ENDC + "" + element.get('action')
                analyse.action = element.get('action')
            except:
                print bcolors.BOLD + "|_action:" + bcolors.ENDC + " NO_ACTION"
            try:
                print bcolors.BOLD + "|_method:" + bcolors.ENDC + "" + element.get('method')
                analyse.method = element.get('method')
            except:
                print bcolors.BOLD + "|_method:" + bcolors.ENDC + " NO_METHOD"
            try:
                print bcolors.BOLD + "|_ID:" + bcolors.ENDC + "" + element.get('id')
            except:
                print bcolors.BOLD + "|_ID:" + bcolors.ENDC + " NO_ID"
            input_all = element.find_all('input')
            analyse.menuForm(input_all)

def follow_link():
    global link_listing
    for link in link_listing:
        print "| "+link
        user_input = raw_input('DOMFf follow this link ? [y/N]')
        if user_input == "y" or user_input == "Y":
            header(link)

def clear_link():
    global link_listing
    link_listing = []
    print bcolors.OKGREEN + "| "+bcolors.ENDC+"Link clear (0)"

def useragent():
    global list_agent
    global user_agent
    action = 0
    found = 0
    print bcolors.WARNING + "| "+bcolors.ENDC+"Please select User-Agent"
    for agent in list_agent:
        print bcolors.BOLD+"| "+bcolors.ENDC+agent['name']
    while action == 0:
        user_agent = raw_input('DOMFf (select agent) > ')
        for agent in list_agent:
            if agent['name'] == user_agent:
                found = 1
                user_agent = agent['string']
                print bcolors.OKGREEN+"| "+bcolors.ENDC+agent['name']+" selected"
                action = 1
        if found < 1:
            print bcolors.FAIL + "| " + bcolors.ENDC + "user-agent not found please select one"
def forensics():
    global web_url
    global log_online
    global header_information
    exit = 0
    forensics_menu()
    while exit == 0:
        if log_online == "on":
            logging_status = bcolors.OKGREEN + log_online + bcolors.ENDC
        else:
            logging_status = bcolors.FAIL + log_online + bcolors.ENDC
        user_input = raw_input("DOMFf : (logging:"+logging_status+") <"+web_url+page_url+"> # ")
        if user_input == "header":
            show_header()
        if user_input == "useragent":
            useragent()
        if user_input == "clear":
            os.system('clear')
        if user_input == "help" or user_input == "ls":
            forensics_menu()
        if user_input == "analyser":
            analyser()
        if "jmp:" in user_input:
            debug(user_input)
        if "jmpdel:" in user_input:
            debug(user_input)
        if "brk:" in user_input:
            debug(user_input)
        if "brkdel:" in user_input:
            debug(user_input)
        if "set:" in user_input:
            debug(user_input)
        if user_input == "bk_url":
            if move_stuct['return'] != "":
                print bcolors.OKBLUE + "| "+bcolors.ENDC + move_stuct['return']
            else:
                print bcolors.OKBLUE + "| " + bcolors.ENDC + "No back url"
        if user_input == "mov":
            debug(user_input)
        if user_input== "reboot":
            header(web_url)
        if user_input == "get_form":
            get_form()
        if user_input == "import_link":
            import_link()
        if user_input == "map_link":
            map_link()
        if user_input == "network":
            network()
        if user_input == "clear_link":
            clear_link()
        if user_input == "cookie":
            add_cookie()
        if "log:" in user_input:
            s_logs(user_input)
        if user_input == "exit":
            exit = 1
            sys.exit()

def add_cookie():
    global global_cookie
    if global_cookie != "":
        print bcolors.WARNING + "| Cookie already set"+bcolors.ENDC
        user_input = raw_input('DOMFf : Update cookie (y/N) # ')
        if user_input == "y" or user_input == "Y":
            cookie = raw_input(bcolors.BOLD + 'DOMFf : New cookie # '+bcolors.ENDC)
            global_cookie = cookie
            print bcolors.OKGREEN + "| Cookie updated"+bcolors.ENDC
    else:
        cookie = raw_input(bcolors.BOLD+'DOMFf : New cookie # '+bcolors.ENDC)
        global_cookie = cookie
        print bcolors.OKGREEN + "| Cookie updated" + bcolors.ENDC

def s_logs(line):
    global log_online
    global log_file
    if "log:" in line:
        separate = line.split('log:')
        if not " " in separate[1]:
            logs_class = listen_logs()
            if separate[1] == "on" or separate[1] == "ON":
                log_online = "on"
                logs_class.start()
            elif separate[1] == "off" or separate[1] == "OFF":
                log_online = "off"
                logs_class.stop()
def get_source(url,pages, header,html,move_cmd=False):
    global header_information
    global web_url
    global page_url
    web_url = url
    page_url = pages
    header_information = header
    global source_code
    source_code = html
    loading = 0
    if move_cmd == True:
        analyser()
    else:
        while loading != 100:
            os.system('clear')
            print "Loading forensic tools ("+str(loading)+'/100)'
            loading += 10
            time.sleep(0.1)
        os.system('clear')
        forensics()

redirect = False
error = False
information_status = {'301':{'status':"permanent URL redirection (301)",
                             'redirect':True,
                             'error':False},
                      '302':{'status':"temporary URL redirect (302)",
                             'redirect':True,
                             'error':False},
                      '300':{'status':"Multiple Choices (300)",
                             'redirect':True,
                             'error':False},
                      '401':{'status':"Restricted access (401)",
                             'redirect':False,
                             'error':True},
                      '404':{'status':"Page not found (404)",
                             'redirect':False,
                             'error':True},
                      '418':{'status':"I'm a teapot (418)",
                             'redirect':False,
                             'error':True},
                      '500':{'status':"Internet error (500)",
                             'redirect':False,
                             'error':True},
                      '200':{'status':"Perfect loading (OK)",
                             'redirect':False,
                             'error':False
                             },
                      '400':{'status':"Bad request (400)",
                             'redirect':False,
                             'error':True
                             }
                      }

def header(url,redirect_cmd=False,move_cmd=False):
    global redirect
    global error
    global user_agent
    global  global_cookie
    if not redirect_cmd:
        if '://' in url:
            http_value = url.split('://')[0]
            new_url = url.split('://')[1]
            if "/" in new_url:
                pages = new_url.split('/')[1:]
                pages = '/'+'/'.join(pages)
                url = http_value+"://"+new_url.split('/')[0]
            else:
                pages = "/"
    else:
        new_url = url.split('://')[1]
        if "/" in new_url:
            url = url.split('://')[0] + '://' + new_url.split('/')[0]
            pages = new_url.split('/')[1:]
            pages = '/'+'/'.join(pages)
        else:
            pages = "/"
    try:
        header_useragent = {'User-Agent': user_agent,'Cookie':global_cookie}
        connexion = urllib2.Request(url+pages, None, header_useragent)
        response = urllib2.urlopen(connexion)
        headers = response.info()
        code_stats = information_status[str(response.getcode())]
    except:
        print "| "+url+pages
        print bcolors.FAIL + "| Service or domain not found."+bcolors.ENDC
        sys.exit()
    print bcolors.OKGREEN + "| " + code_stats["status"] + bcolors.ENDC
    if code_stats['redirect']:
        redirect = True
    elif code_stats['error']:
        error = True
    for line in headers:
        if "location" in line:
            print bcolors.OKBLUE + "|_" + line
            if redirect:
                user_input = raw_input(bcolors.WARNING + "[+] Moved to : " + line[1] + " follow? [Y/n]"+bcolors.ENDC)
                if user_input == "" or user_input == "Y" or user_input == "y":
                    print response.status
                    redirect = False
                    header(line[1], True)
        print bcolors.OKBLUE + "| "+line + ":" + line + bcolors.ENDC
    if move_cmd:
        get_source(url, pages, headers, response.read(),move_cmd=True)
    else:
        user_input = raw_input(bcolors.BOLD + "| Load tools <enter> : "+bcolors.ENDC)
        if user_input == "" or user_input == "Y" or user_input == "y":
            get_source(url,pages, headers,response.read())