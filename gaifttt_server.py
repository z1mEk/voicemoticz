from flask import Flask
app = Flask(__name__)

@app.route("/say/?text=<phrase>")
def say():
    return "Say
    
if __name__ == '__main__':
app.run(host='0.0.0.0', port=8082) 
