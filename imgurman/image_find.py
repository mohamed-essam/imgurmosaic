from imgurpython import ImgurClient

client_id = '86e36c27dc88fb7'
client_secret = '7e88eb8aaebcc8b864f5ecb0d06ecfe5523e8000'

client = ImgurClient(client_id, client_secret)

items = client.gallery_search(q='cats', sort='top', window='week')
links = []
for item in items:
    links.append(item.link)

def getCatPic():
    return links;
