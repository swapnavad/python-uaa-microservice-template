# python-uaa-mircoservice-starter
THis is a sample application integrated with predix UAA to show case authoce workflow with python.The application landing page, will show a login link.The login link will redirect users to Predix UAA login page ,promting the user to input username and password. Once the user has successfully logged in the UAA redirects user back to the using the redirect url. In this application the redirect URL is "/callback". The callback endpoint calls the oauth workflow to get access_token from the UAA, then redirects the users to "/secure" endpoint. The "/secure" endpoint,checks the existance of token in the session. If the token is found it displays a Login message,otherwise indicates the to the user to login with Predix UAA.

This application is based on Flask ,requests and gunicorn as documented on the requirement.txt file. The requirement.txt is necessary and defines the python modules.The python buildpack at cf push process, pulls in these python modules. The manifest.yml has the startup command for the application.


## Deploy to cloud
Please login to the predix account using cf login
* git clone <*this repository*>
  Edit the manifest.yml
  * add the uaa instance to the list of services,
  * set client_id and base64encodedClientDetails
* cf push <*your-appname*>


## Running Locally
Please login to the predix account using cf login
* git clone <*this repository*>
  Edit the application-controller.py to set the UAA details.
    * CLIENT_ID : change this to client_id you have created on UAA
    * UAA_URL : UAA URI of the UAA
    * BASE64ENCODING : change this  to base64 encoding of clientid:secret
