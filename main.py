from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return 'Hello, World! <3. This is v1.0.1 of the python app and is hosted on kubernetes'
 
 
if __name__ == "__main__":
    app.run()
