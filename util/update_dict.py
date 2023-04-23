import requests
import gzip

# Dictionaries: JMdict (w/ examples), Kanjidic
dicts = ["http://ftp.edrdg.org/pub/Nihongo/JMdict_e_examp.gz"]

def update_dicts():
    for url in dicts:
        words = url.split('/')
        req = requests.get(url, allow_redirects=True)
        open('dicts/' + words[-1], 'wb').write(req.content)
        
        open('dicts/test', 'wb'.write(gzip.decompress(gzip.open('dicts/' + words[-1], 'wb')))
