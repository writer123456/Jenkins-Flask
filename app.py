from flask import Flask
# flask application runs on port 5000
#add commands to install python and flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True)
