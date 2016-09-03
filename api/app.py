from flask import Flask, request
from imgurman import getCatPic
from mosaic import get_mosaic
from tempfile import NamedTemporaryFile

application = Flask(__name__)

@application.route('/')
def fu():
    links = getCatPic()
    print(len(links))
    rem = links[1:4]
    get_mosaic(links[0], rem)
