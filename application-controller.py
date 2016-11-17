"""
Python Sample Microservice for Predix

Author: 212421693

"""
from flask import Flask, request ,redirect ,session
from uuid import uuid4
import requests
import requests.auth
import urllib
import base64
import os
import json

## SET this only for local testing, if VCAPS is set env they will be overwritten by VCAPS.
CLIENT_ID = None # "app_client_id"
UAA_URL= None #"https://9c5f79c3-9760-47fc-b23f-0beba4525e10.predix-uaa.run.aws-usw02-pr.ice.predix.io"
BASE64ENCODING = None #'YXBwX2NsaWVudF9pZDpzZWNyZXQ='
port = int(os.getenv("PORT", 9099))
REDIRECT_URI = None #"http://localhost:"+str(port)+"/callback"

## Setting up Oauth2 , this values should be read from vcaps .
APP_URL= None
# Get UAA credentials from VCAPS
if 'VCAP_SERVICES' in os.environ:
    services = json.loads(os.getenv('VCAP_SERVICES'))
    uaa_env = services['predix-uaa'][0]['credentials']
    UAA_URL=uaa_env['uri']

# Get UAA credentials from VCAPS
if 'VCAP_APPLICATION' in os.environ:
    applications = json.loads(os.getenv('VCAP_APPLICATION'))
    app_details_uri = applications['application_uris'][0]
    APP_URL = 'https://'+app_details_uri
    REDIRECT_URI = APP_URL+'/callback'
else :
    APP_URL = "http://localhost:"+str(port)
    REDIRECT_URI = APP_URL+"/callback"

if(os.getenv('client_id')):
    CLIENT_ID = os.getenv('client_id')

if(os.getenv('base64encodedClientDetails')):
    BASE64ENCODING = os.getenv('base64encodedClientDetails')

app = Flask(__name__)
# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

###### Setting up REST endpoints :

@app.route('/')
def home():
    print 'Calling root resource'
    text = '<br> <a href="%s">Authenticate with Predix UAA </a>'
    return 'Hello from Python microservice template!'+text % getUAAAuthorizationUrl()

@app.route('/secure')
def securepage():
    print 'securepage '
    key = session.get('key', 'not set')
    if 'access_token' in session:
        # TODO: call to Check_token to validate this token
        return 'This is a secure page,gated by UAA'
    else :
        text = '<br> <a href="%s">Authenticate with Predix UAA </a>'
        return 'Token not found, You are not logged in to UAA '+text % getUAAAuthorizationUrl()

## Auth-code grant-type required UAA
@app.route('/callback')
def UAAcallback():
    print 'callback '
    error = request.args.get('error', '')
    if error:
        return "Error: " + error
    state = request.args.get('state', '')
    if not is_valid_state(state):
        # Uh-oh, this request wasn't started by us!
        abort(403)
    code = request.args.get('code')
    access_token = get_token(code)
    # TODO: store the user token in sesson or redis cache , but for now use Flask session
    session['access_token'] = access_token
    return redirect(APP_URL+"/secure", code=302)
    print "You have logged in using UAA  with this access token %s" % access_token


# method to consttruct Oauth authorization request
def getUAAAuthorizationUrl():
    state = 'secure'
    params = {"client_id": CLIENT_ID,
              "response_type": "code",
              "state": state,
              "redirect_uri": REDIRECT_URI
              }
    url = UAA_URL+"/oauth/authorize?" + urllib.urlencode(params)
    return url

# Oauth Call to get access_token based on code from UAA
def get_token(code):
    post_data = {"grant_type": "authorization_code",
                 "code": code,
                 "redirect_uri": REDIRECT_URI,
                 "state":"secure"}
    headers = base_headers()
    response = requests.post(UAA_URL+"/oauth/token",
                             headers=headers,
                             data=post_data)
    token_json = response.json()
    return token_json["access_token"]

def base_headers():
    return {"Authorization": "Basic "+BASE64ENCODING }

def is_valid_state(state):
    if(state == 'secure' ) :
        return True
    else :
        return False

if __name__ == '__main__':
    # Run the app, listening on all IPs with our chosen port number
    app.run(host='0.0.0.0', port=port)
    #app.run(debug=True)
