# python-mircoservice-starter
This is a sample hello microservice template for python.This application is based on Flask and gunicorn as documented on the requirement.txt file. The requirement.txt is necessary and defines the python modules.The predix python buildpack at cf push process, pulls in these python modules. The manifest.yml has the startup command for the application. 

## Steps
Please login to the predix account using cf login 
* git clone <*this repository*>
* cf push <*your-appname*>
