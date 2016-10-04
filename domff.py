#!/usr/env/python
# -*- coding: utf-8 -*-

import sys
import random
from func.body import *

base_url = ""

def print_logo():

    logo_a =  """
 ▄▀▀█▄▄   ▄▀▀▀▀▄   ▄▀▀▄ ▄▀▄  ▄▀▀▀█▄    ▄▀▀▀█▄
█ ▄▀   █ █      █ █  █ ▀  █ █  ▄▀  ▀▄ █  ▄▀  ▀▄
▐ █    █ █      █ ▐  █    █ ▐ █▄▄▄▄   ▐ █▄▄▄▄
  █    █ ▀▄    ▄▀   █    █   █    ▐    █    ▐
 ▄▀▄▄▄▄▀   ▀▀▀▀   ▄▀   ▄▀    █         █
█     ▐           █    █    █         █
▐                 ▐    ▐    ▐         ▐
"""

    logo_b = """
·▄▄▄▄        • ▌ ▄ ·. ·▄▄▄·▄▄▄
██▪ ██ ▪     ·██ ▐███▪▐▄▄·▐▄▄·
▐█· ▐█▌ ▄█▀▄ ▐█ ▌▐▌▐█·██▪ ██▪
██. ██ ▐█▌.▐▌██ ██▌▐█▌██▌.██▌.
▀▀▀▀▀•  ▀█▄▀▪▀▀  █▪▀▀▀▀▀▀ ▀▀▀
    """

    logo_c = """
██████╗  ██████╗ ███╗   ███╗███████╗███████╗
██╔══██╗██╔═══██╗████╗ ████║██╔════╝██╔════╝
██║  ██║██║   ██║██╔████╔██║█████╗  █████╗
██║  ██║██║   ██║██║╚██╔╝██║██╔══╝  ██╔══╝
██████╔╝╚██████╔╝██║ ╚═╝ ██║██║     ██║
╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚═╝
"""
    logo_nb = random.randint(1,3)
    if logo_nb == 1:
        print logo_a
    elif logo_nb == 2:
        print logo_b
    else:
        print logo_c

def check_argv():
    for argv in sys.argv:
        if len(sys.argv) < 2:
            print bcolors.FAIL + "| " + bcolors.ENDC + "Please use : python " + sys.argv[0] + " --url=http://exemple.com"
        elif "--url=" in sys.argv[1]:
            url_information = sys.argv[1].split('--url=')
            if "://" in url_information[1] or "www." in url_information[1]:
                if "." in url_information[1]:
                    if "www." in url_information[1] and not "://" in url_information[1]:
                        url_information[1] = "http://" + url_information[1]
                    base_url = url_information[1]
                    header(base_url)
        else:
            print bcolors.FAIL + "| "+bcolors.ENDC + "Please use : python "+sys.argv[0]+" --url=http://exemple.com"
def main():
    print_logo()
    check_argv()
main()