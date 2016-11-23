#!/usr/env/python
# -*- coding: utf-8 -*-

import sys
import random
from core.autoload import *

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

def main():
    print_logo()
    print bcolors.OKGREEN + "---"+bcolors.ENDC
    print bcolors.BOLD + "Twitter: "+bcolors.ENDC+"@graniet75"
    print bcolors.OKGREEN + "---" + bcolors.ENDC
    load = AutoLoad(sys.argv)
    load.domff()

if __name__ == '__main__':
    main()