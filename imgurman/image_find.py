from imgurpython import ImgurClient
from random import shuffle

client_id = '86e36c27dc88fb7'
client_secret = '7e88eb8aaebcc8b864f5ecb0d06ecfe5523e8000'

client = ImgurClient(client_id, client_secret)

def getCatPic(allowGallery=False):
    items = client.gallery_search(q='cats', sort='top', window='day')
    links = []
    for item in items:
        if(item.is_album and allowGallery):
            x = client.get_album(item.id)
            for img in x.images:
                if(img['type'] == 'image/jpeg'):
                    links.append(img['id'])
        elif(not item.is_album):
            if(item.type == 'image/jpeg'):
                links.append(item.id)
    for i in range(0, len(links)):
        links[i] = 'http://imgur.com/' + links[i]
    shuffle(links)
    return links;
