from flask import Flask, jsonify 

app = Flask(__name__)
@app.route("//",methods=["GET", "POST"])
def welcome (): 
    nv = {1:3,2:4,5:66,6:7}
    return nv

if __name__ == "__main__":
    app.run(host = "0.0.0.0")
