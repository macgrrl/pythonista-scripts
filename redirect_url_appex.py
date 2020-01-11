import appex
import console
import re
import requests
import webbrowser

# functions

def show_alert(s):
    console.alert('Alert', s, 'OK', hide_cancel_button=True)


# Main program

starturl = appex.get_url()

#show_alert(starturl)

response = requests.request('GET', starturl, allow_redirects=True)
bin_content = response.content

content = bin_content.decode('UTF-8')
#show_alert(content)

regex = re.compile(r'redirecturl = \'(https?://.*)\'')

regex_match = regex.search(content)

if regex_match != None:
    redirect_url = regex_match.group(1)
    #show_alert(redirect_url)
    # launch instapaper x-url
    #instapaper_xurl = 'x-callback-instapaper://x-callback-url/add?url='
    #response = requests.request('GET', instapaper_xurl + redirect_url)
    webbrowser.open('workflow://run-workflow?name=Instapaper%20URL&input=' + redirect_url)
else:
    show_alert('No match...')

