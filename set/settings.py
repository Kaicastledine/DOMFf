# Theme configuration (Please carreful with analyzer)
theme = {'BOLD':
             ['<meta','<title>','<link',' />','<html','<head','</title>','<script>','<script','</script>'],
         'GREEN':
             ['crossorigin=','content=','prefix=','lang=','integrity=','media=','rel=','http-equiv=','name=','value=','rel='],
         'YELLOW':
             ['']
         }

# Configuration for useragent
list_agent = [
    {'name':'Chrome','string':'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19'},
    {'name':'Chromium','string':'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Ubuntu/10.10 Chromium/8.0.552.237 Chrome/8.0.552.237 Safari/534.10'},
    {'name':'Firefox','string':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1b3) Gecko/20090305 Firefox/3.1b3 GTB5'},
    {'name':'W3C_Validator','string':'W3C_Validator/1.654'},
    {'name':'LynxFramework','string':'Lynxframework'}
]