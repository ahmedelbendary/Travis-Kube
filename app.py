from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, From AhmedElbendary/Travis account !!\n R1.0.0-dev Deploy on kubernetes cluster dev namespace'  