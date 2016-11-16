from func.color import *
import urllib2
from func.body import *

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

def header(url,redirect_cmd=False):
    global redirect
    global error
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
    header_useragent = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36"}
    connexion = urllib2.Request(url, None, header_useragent)
    response = urllib2.urlopen(connexion)
    headers = response.info()
    code_stats = information_status[str(response.getcode())]
    print bcolors.OKGREEN + "[+] " + code_stats["status"] + bcolors.ENDC
    if code_stats['redirect']:
        redirect = True
    elif code_stats['error']:
        error = True
    for line in headers:
        if "location" in line:
            print "cotcot"
            print bcolors.OKBLUE + "|_" + line
            if redirect:
                user_input = raw_input(bcolors.WARNING + "[+] Moved to : " + line[1] + " follow? [Y/n]"+bcolors.ENDC)
                if user_input == "" or user_input == "Y" or user_input == "y":
                    print response.status
                    redirect = False
                    header(line[1], True)
        print bcolors.OKBLUE + "| "+line + ":" + line + bcolors.ENDC
    user_input = raw_input(bcolors.BOLD + "[+] Start analyse <" + pages + "> ? [Y/n] : " + bcolors.ENDC)
    if user_input == "" or user_input == "Y" or user_input == "y":
        get_source(url,pages, headers,response.read())