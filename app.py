from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, From AhmedElbendary/Travis account !!\n This is my first Task in Ocucon'  