# Import necessary libraries for our app

from flask import Flask, request, jsonify
from datetime import datetime

# Initialize Flask app (this creates an instance of the Flask web application)
app = Flask(__name__)

# Define a route (URL endpoint) that listens for GET requests on the root URL "/"
@app.route('/', methods=['GET'])
def get_time_and_ip():
    """
    This function handles GET requests made to the root URL.
    It returns a JSON response containing the current UTC timestamp and the client's IP address.
    """
    return jsonify({
        "timestamp": datetime.utcnow().isoformat() + "Z",  # Get current UTC time in ISO format and add 'Z' to indicate UTC
        "ip": request.remote_addr  # Get the IP address of the client making the request
    })

# Entry point of the Python application
if __name__ == '__main__':
    # Run the Flask application on all available network interfaces (0.0.0.0) and port 80
    # This makes the service accessible from outside the container or host machine
    app.run(host='0.0.0.0', port=80)

