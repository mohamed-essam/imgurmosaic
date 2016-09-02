from flask import Flask, request
app = Flask(__name__)

@app.route('/heil')
def fu():
    return "Heil %s" % request.args.get("name")
