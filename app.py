from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # Get the port from the environment variable `PORT` that Render provides
    # Render sets the `PORT` environment variable, default to 10000 if not provided
    port = int(os.environ.get('PORT', 10000))  # Use 10000 if no port is defined
    app.run(debug=False, host='0.0.0.0', port=port)
