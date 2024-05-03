from flask import Flask , render_template, jsonify , request
from flask_cors import CORS
import os

secret_1 = os.environ.get('SECRET_1')
secret_2 = os.environ.get('SECRET_2')

app = Flask(__name__)
CORS(app)

@app.route('/home/')
def home():
    
    return {'msg':secret_1}

if __name__=="__main__":
    app.run(debug=True)
