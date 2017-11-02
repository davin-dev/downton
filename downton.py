from flask import Flask
from flask import request
import os
import socket
import platform
import urllib
import json
import requests


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) #allow both GET and POST requests
def post_data():
			
        url = request.form.get('url')     #you can change the request method
        name = url[url.rfind("/")+1:]

        urllib.urlretrieve (url,name )
			
				
				

	surl = socket.getfqdn()+"/"+name        #downloaded file url address.
	path = os.getcwd()+name                 #downloaded file server address.
	if os.path.isfile(path) == True:
		
		print 'OK IT IS HERE!'
		return 'OK!'
		payload = {'url':surl, 'name':name }
		jon = json.dumps(payload)
		response = requests.post('YOUR CLIENT ADDRESS HERE', data = jon)
		print(response.text) #TEXT/HTML
		print(response.status_code, response.reason) #HTTP
	
	
	else:
		
		print 'ERROR!'
		return 'ERROR!'
		payload = {'url':'ERROR', 'name':name }
		jon = json.dumps(payload)
		response = requests.post('YOUR CLIENT ADDRESS HERE', data = jon)
		print(response.text) #TEXT/HTML
		print(response.status_code, response.reason) #HTTP
	
	

	
	
#       if you need it just in case..
#        return '''
#                  <h1>your link is ready :  {}</h1>
#                  '''.format(surl)

#       if you need a simple form...

#   	 return '''<form method="POST">
#                  url: <input type="text" name="url"><br>
#                  <input type="submit" value="Submit"><br>
#              </form>'''


			  
			  # FLASK_APP=downton.py flask run --host=0.0.0.0
