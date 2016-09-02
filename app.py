from flask import Flask, request
application = Flask(__name__)

@application.route('/heil')
def fu():
    return "Heil %s" % request.args.get("name")
