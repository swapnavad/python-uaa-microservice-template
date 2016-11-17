# python-mircoservice-starter
This is a sample hello microservice template for python.This application is based on Flask and gunicorn as documented on the requirement.txt file. The requirement.txt is necessary and defines the python modules.The python buildpack at cf push process, pulls in these python modules. The manifest.yml has the startup command for the application.


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
