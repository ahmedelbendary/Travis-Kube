from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, From AhmedElbendary/Travis account !!\n R2.2.2 Deploy on kubernetes cluster'  