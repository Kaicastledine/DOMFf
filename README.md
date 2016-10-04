![header](https://s3.postimg.org/shu3mhtkj/Capture_d_e_cran_2016_10_04_a_15_34_43.png)

# DOMFf
+ DOM FORENSICS FRAMEWORK

#### Start analysis
```bash
python domff.py --url=http://exemple.com
```

#### Menu listing
```
____________________________________________________________
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
------------------------------------------------------------
```

##### header (MENU)
+ Show header information
+ exemple :
```
DOMFf : (logging:off) <http://github.com/graniet/> # header
| Server: GitHub.com
| Date: Tue, 04 Oct 2016 13:31:29 GMT
| Content-Type: text/html; charset=utf-8
| Transfer-Encoding: chunked
| Connection: close
| Status: 200 OK
| Cache-Control: no-cache
| Vary: X-PJAX
.....
```

##### useragent (MENU)
+ Show list of useragent
+ exemple :
```
DOMFf : (logging:off) <http://github.com/graniet/> # useragent
| Please select User-Agent
| Chrome
| Chromium
| Firefox
| W3C_Validator
| LynxFramework
```

##### cookie (MENU)
+ Change current cookie
+ exemple:
```
DOMFf : (logging:off) <http://github.com/graniet/> # cookie
DOMFf : New cookie # (Enter new cookie here)
```

##### analyser (IDE)
+ load analyser IDE
+ exemple:
```
| starting forensics with jmp <>
|0x0|<!DOCTYPE html>
|0x1|<html lang="en" class=" is-copy-enabled emoji-size-boost is-u2f-enabled">
|0x2|<head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object:...
|0x3|<meta charset='utf-8'>
|0x4|<meta content="origin-when-cross-origin" name="referrer" />
|0x5|
|0x0|<enter> or <help>:
.... 

```

##### get_form (MENU)
+ get all form in source
+ exemple:
```
DOMFf : (logging:off) <http://github.com/graniet/> # get_form
http://github.com
|__/graniet/
|_type : FORM (NO_NAME)
|_action:/search
|_method:get
|_ID: NO_ID
____________________________________________________________
| show             : Show params loaded data.
| sqlmap           : Generate SQLMAP line with current params.
| vuln             : Show possible vulnerability.
| help             : Show this help bullet.
| <enter>          : Skip this data.
------------------------------------------------------------
DOMFf:FORM >
```

#### jmp (MENU)
+ Configure one jump with jmp:<tag>
+ exemple : 
```
DOMFf : (logging:off) <http://github.com/graniet/> # jmp:a
| (<a>) element added to jump list
```

+ Show all jump with jmp:list
+ exemple :
```
DOMFf : (logging:off) <http://github.com/graniet/> # jmp:list
| <a>
```

+ Delete one jump with jumpdel:<tag>
+ exemple:
```
DOMFf : (logging:off) <http://github.com/graniet/> # jmpdel:a
| element <a> removed
```

##### Breakpoint (MENU)
+ Configure one breakpoint with brk:<tag>
+ exemple:
```
DOMFf : (logging:off) <http://github.com/graniet/> # brk:a
| breaking on <a>
```

+ Show all breakpoint with brk:list
+ exemple:
```
DOMFf : (logging:off) <http://github.com/graniet/> # brk:list
| <a>
```

+ Delete one breakpoint with brkdel:<tag>
+ exemple:
```
DOMFf : (logging:off) <http://github.com/graniet/> # brkdel:a
| element <a> removed
```

##### Configure new url (MENU)
+ set new url with set:<url>
+ exemple:
```
DOMFf : (logging:off) <http://github.com/graniet/> # set:http://github.com
| new url : http://github.com
```

+ load new url with mov
+ exemple:
```
...
| Perfect loading (OK)
| status:status
| x-request-id:x-request-id
| x-xss-protection:x-xss-protection
| x-content-type-options:x-content-type-options
| content-security-policy:content-security-policy
| transfer-encoding:transfer-encoding
| set-cookie:set-cookie
| strict-transport-security:strict-transport-security
... 
| Load tools <enter> :
```

##### reboot (MENU)
+ for reboot current interface use : reboot

##### import all link
+ for import all source link use : import_link
+ exemple:
```
DOMFf : (logging:off) <http://github.com/> # import_link
| New link imported : http://github.com/#start-of-content
| New link imported : https://help.github.com/articles/supported-browsers
| New link imported : https://www.apple.com/safari/
| New link imported : https://chrome.google.com
| New link imported : https://mozilla.org/firefox/
| New link imported : https://github.com/
| New link imported : http://github.com/personal
| New link imported : http://github.com/open-source
...
```

##### Show map (MENU)
+ For check all mapping link use : map_link

##### show session network (MENU)
+ For show session network use : network
+ exemple:
```
DOMFf : (logging:off) <http://github.com/graniet> # network
|http://github.com/
 |http://github.com/granietc
```

##### Logs
+ For start logging use : log:on
+ exemple:
```
DOMFf : (logging:off) <http://github.com/graniet> # log:on
| Listen logs start : /....domff/logs/be2d8e1a-7665-471c-a69a-2cd342fc4197.domff
```

+ For stop logging use : log:off
+ exemple:
```
DOMFf : (logging:on) <http://github.com/graniet> # log:off
| Listen logs stop
```


#### IDE PLUGINS

+ SOON