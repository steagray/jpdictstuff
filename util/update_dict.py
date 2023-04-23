import requests
import gzip
import os

# URL to dictionaries to download 
# JMdict (w/ examples)
dicts = ["http://ftp.edrdg.org/pub/Nihongo/JMdict_e_examp.gz"]

# For each entry in the dicts array, downloads the gz file, and then decompresses it
# Uses the final segment of the url to determine the filename
def update_dicts():
    for url in dicts:
        words = url.split('/')
        req = requests.get(url, allow_redirects=True)
        if req.status_code != requests.codes.ok:
            print("Unable to get ", words[-1])
            return

        try:
            open('dicts/' + words[-1], 'wb').write(req.content)
        except FileNotFoundError:
            os.mkdir('dicts')
            open('dicts/' + words[-1], 'wb').write(req.content)

        with gzip.open('dicts/' + words[-1], 'rb') as g:
            with open('dicts/' + words[-1][:-3:1], 'wb') as f:
                f.write(g.read())
        os.remove("dicts/" + words[-1])
