# Import the Flask module
from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define the route for the root URL ("/")
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run the app if this script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

