from flask import Flask , render_template, jsonify , request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/home/')
def home():
    return {'msg':'this is the home'}

if __name__=="__main__":
    app.run(debug=True)
