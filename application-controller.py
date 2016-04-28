"""
Python Simulator for Predix

Author: 212421693

"""
from flask import Flask
import os

app = Flask(__name__)

# Get port from environment variable or choose 9099 as local default
port = int(os.getenv("PORT", 9099))

@app.route('/')
def home():
    print 'Calling root resource'
    return 'Hello from Python microservice template! I am instance ' + str(os.getenv("CF_INSTANCE_INDEX", 1) + ' and tagged as ' +str(os.getenv('TAG_NAME')))


if __name__ == '__main__':
    # Run the app, listening on all IPs with our chosen port number
    app.run(host='0.0.0.0', port=port)
