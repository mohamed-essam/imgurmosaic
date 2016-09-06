from flask import Flask, request, Response
from imgurman import getCatPic
from mosaic import get_mosaic
from tempfile import NamedTemporaryFile
from base64 import b64encode
import os
from time import sleep


application = Flask(__name__)

@application.route('/')
def fu():
    max_limit = int(request.args['tileCount'])
    shit = int(request.args.get('sourceIndex', 0))
    allowGallery = bool(request.args.get('allowGallery', True))
    links = getCatPic(allowGallery)
    if(max_limit > len(links)):
        max_limit = len(links)
    if(max_limit < 2):
        max_limit = 2
    res = links[0:shit] + links[shit+1:max_limit]
    for i in range(0, len(res)):
        res[i] = res[i] + 's.jpg'

    img = get_mosaic(links[shit]+'.jpg', res)
    last_size = 0
    while(last_size == 0 or os.stat(img.name).st_size != last_size):
        last_size = os.stat(img.name).st_size
        sleep(0.5)
    f = open(img.name, 'r')
    ret = f.read()
    f.close()
    img.close()
    return Response(ret, mimetype="image/png")
