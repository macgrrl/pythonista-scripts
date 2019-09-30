import appex
import re
import requests
import webbrowser

starturl = appex.get_text()

response = requests.request('GET', starturl, allow_redirects=True)
bin_content = response.content

content = bin_content.decode('UTF-8')
print(content)

regex = re.compile(r'redirecturl = \'(https?://.*)\'')

regex_match = regex.search(content)

if regex_match != None:
    print('Match made!')
    redirect_url = regex_match.group(1)
    print(redirect_url)
    # launch instapaper x-url
    #instapaper_xurl = 'x-callback-instapaper://x-callback-url/add?url='
    #response = requests.request('GET', instapaper_xurl + redirect_url)
    webbrowser.open('workflow://run-workflow?name=Make%20PDF&input=text&text=soup
redirect_url)
else:
    print('No match...')
